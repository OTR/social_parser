"""
duration

any — не фильтровать результаты поиска видео по их продолжительности. Это значение по умолчанию.
long — включайте только видео продолжительностью более 20 минут.
medium – включать только видео продолжительностью от четырех до 20 минут (включительно).
short – включайте только видео продолжительностью менее четырех минут.
"""
import os
import time
from pathlib import Path
from ssl import SSLEOFError

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from data.file_logger import FileLogger
from data.youtube.csv_key_value_storage import CSVKeyValueStorage
from data.youtube.dto.comment_dto import CommentDTO
from data.youtube.dto.youtube_dto import YoutubeDTO
from data.youtube.dto.video_dto import VideoDTO
from data.youtube.key_rotator import KeyRotator
from data.youtube.mapper.comment_mapper import CommentMapper
from data.youtube.mapper.video_mapper import VideoMapper
from exception.youtube_no_available_keys_to_rotate import YoutubeNoAvailableKeysToRotateTo

PATH_TO_PROJECT_ROOT = Path(__file__).parent.parent.parent
PATH_TO_ENVIRONMENT_VARIABLES = PATH_TO_PROJECT_ROOT / "python_anywhere.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)


class YoutubeApiClient:
    """"""
    _PATH_TO_KEY_STORAGE = PATH_TO_PROJECT_ROOT /  ".data" / "key_storage.csv"
    _YOUTUBE_API_SERVICE_NAME = "youtube"
    _YOUTUBE_API_VERSION = "v3"
    _DEFAULT_KEYWORD = os.getenv("DEFAULT_KEYWORD")
    _QUOTA_REASON: str = (
        'The request cannot be completed because you have exceeded your ' +
        '<a href="/youtube/v3/getting-started#quota">quota</a>.'
    )
    _MAX_RETRIES = 5

    def __init__(self, api_client=None, key_rotator=None, logger=None):
        """"""
        keys = os.getenv("YOUTUBE_DATA_API_V3_KEYS")
        self._key_rotator = key_rotator or self._instantiate_key_rotator(keys)
        current_key = self._key_rotator.get_current_key()
        self._youtube_object = api_client or self._build_youtube_object(current_key)
        self._logger = logger or FileLogger().get_logger()

    def get_latest_videos(
            self,
            keyword=None,
            max_results=50,
            page_token="",
            duration="any"
    ) -> YoutubeDTO:
        """"""
        query: str = keyword if keyword is not None else self._DEFAULT_KEYWORD
        search_response = {}

        def make_request():
            return self._youtube_object.search().list(
                q=query,
                order="date",
                type="video",
                safeSearch="none",
                videoDuration=duration,
                regionCode="RU",
                part="id, snippet",
                maxResults=max_results,
                pageToken=page_token
            ).execute()

        search_response = self._retry_request(make_request)

        next_page_token: str = search_response.get("nextPageToken", "")
        prev_page_token: str = search_response.get("prevPageToken", "")
        entities: list = search_response.get("items", [])
        dtos: list[VideoDTO] = []
        for entity in entities:
            dtos.append(VideoMapper.json_to_dto(entity))

        return YoutubeDTO(
            next_page_token=next_page_token,
            prev_page_token=prev_page_token,
            entities=dtos
        )

    def get_comments_to_video(
            self,
            video_id,
            max_results=100,
            moderation_status="published",
            order="time",
            text_format="plainText",
            page_token=""
    ) -> YoutubeDTO:
        """"""
        try:
            search_response: dict = self._youtube_object.commentThreads().list(
                part="snippet,id",
                maxResults=max_results,
                moderationStatus=moderation_status,
                order=order,
                textFormat=text_format,
                videoId=video_id,
                pageToken=page_token
            ).execute()
        except HttpError as err:
            if err.status_code == 403 and err.reason == YoutubeApiClient._QUOTA_REASON:
                # TODO LOGGING
                print("Quota exceeded")
            search_response = {}
        next_page_token: str = search_response.get("nextPageToken", "")
        entities: list = search_response.get("items", [])
        dtos: list[CommentDTO] = []
        for entity in entities:
            dtos.append(CommentMapper.to_dto(entity))

        return YoutubeDTO(
            next_page_token=next_page_token,
            prev_page_token="",
            entities=dtos
        )

    def _build_youtube_object(self, key: str):
        """Builds and returns a YouTube API client object."""
        return build(
            self._YOUTUBE_API_SERVICE_NAME,
            self._YOUTUBE_API_VERSION,
            developerKey=key
        )

    def _rotate_key(self):
        """Rotates the API key and rebuilds the YouTube client."""
        try:
            new_key = self._key_rotator.rotate_key()
            self._logger.info(f"Rotating to new API key: {new_key}")
            self._youtube_object = self._build_youtube_object(new_key)
        except YoutubeNoAvailableKeysToRotateTo as err:
            pass
        except Exception as e:
            self._logger.error(f"Failed to rotate key: {e}")
            raise e

    def _retry_request(self, func, *args, **kwargs):
        """Retries the given function with exponential backoff."""
        attempt = 0
        while attempt < self._MAX_RETRIES:
            try:
                return func(*args, **kwargs)
            except HttpError as err:
                if err.status_code == 403 and YoutubeApiClient._QUOTA_REASON in err.reason:
                    self._logger.debug(f"Quota exceeded for key: {self._key_rotator.get_current_key()}")
                    self._key_rotator.record_quota_exceeded()
                    self._rotate_key()
                elif attempt < self._MAX_RETRIES - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    self._logger.debug(f"Retrying after {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    self._logger.error("Maximum retries exceeded. Failing the request.")
                    raise err
            except SSLEOFError as err:
                self._logger.debug("Caught SSL EOF Exception", err)
                if attempt < self._MAX_RETRIES - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    self._logger.debug(f"Retrying after {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    self._logger.error("Maximum retries exceeded. Failing the request.")
                    raise err
            except Exception as err:
                self._logger.error(err)
                raise err

            attempt += 1

    @staticmethod
    def _instantiate_key_rotator(keys: str) -> KeyRotator:
        # TODO: require keys not blank
        storage_file = YoutubeApiClient._PATH_TO_KEY_STORAGE
        storage = CSVKeyValueStorage(str(storage_file))
        keys: list[str] = keys.split(";")
        return KeyRotator(keys, storage)
