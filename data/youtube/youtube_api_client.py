"""
duration

any — не фильтровать результаты поиска видео по их продолжительности. Это значение по умолчанию.
long — включайте только видео продолжительностью более 20 минут.
medium – включать только видео продолжительностью от четырех до 20 минут (включительно).
short – включайте только видео продолжительностью менее четырех минут.
"""
import os
from pathlib import Path
from ssl import SSLEOFError

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from data.youtube.youtube_dto import YoutubeDTO
from data.youtube.video_dto import VideoDTO
from data.youtube.video_mapper import VideoMapper
from data.youtube.comment_dto import CommentDTO
from data.youtube.comment_mapper import CommentMapper

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "python_anywhere.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)


class YoutubeApiClient:
    """"""

    _QUOTA_REASON: str = (
        'The request cannot be completed because you have exceeded your ' +
        '<a href="/youtube/v3/getting-started#quota">quota</a>.'
    )

    def __init__(self):
        """"""
        self._YOUTUBE_DATA_API_V3_KEY = os.getenv("YOUTUBE_DATA_API_V3_KEY")
        self._YOUTUBE_API_SERVICE_NAME = "youtube"
        self._YOUTUBE_API_VERSION = "v3"
        self._DEFAULT_KEYWORD = os.getenv("DEFAULT_KEYWORD")
        self._youtube_object = build(
            self._YOUTUBE_API_SERVICE_NAME,
            self._YOUTUBE_API_VERSION,
            developerKey=self._YOUTUBE_DATA_API_V3_KEY
        )

    def get_latest_videos(
            self,
            keyword=None,
            max_results=50,
            page_token="",
            duration="any"
    ) -> YoutubeDTO:
        """"""
        query: str = keyword if keyword is not None else self._DEFAULT_KEYWORD
        try:
            search_response: dict = self._youtube_object.search().list(
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
        except HttpError as err:
            if err.status_code == 403 and err.reason == YoutubeApiClient._QUOTA_REASON:
                # TODO LOGGING
                print("Quota exceeded")
        except SSLEOFError as err:


            search_response = {}
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
