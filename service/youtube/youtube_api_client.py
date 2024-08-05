""""""
import os
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from service.youtube.youtube_dto import YoutubeDTO
from service.youtube.video_dto import VideoDTO
from service.youtube.youtube_mapper import YoutubeMapper

load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")


class YoutubeApiClient:
    """"""
    QUOTA_REASON: str = ('The request cannot be completed because you have exceeded your '
                         '<a href="/youtube/v3/getting-started#quota">quota</a>.')

    def __init__(self):
        """"""
        self.YOUTUBE_DATA_API_V3_KEY = os.getenv("YOUTUBE_DATA_API_V3_KEY")
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"
        self.DEFAULT_KEYWORD = os.getenv("DEFAULT_KEYWORD")
        self.youtube_object = build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.YOUTUBE_DATA_API_V3_KEY
        )

    def get_latest_videos(self, keyword=None, max_results=50, page_token="") -> YoutubeDTO:
        """"""
        query: str = keyword if keyword is not None else self.DEFAULT_KEYWORD
        try:
            search_response: dict = self.youtube_object.search().list(
                q=query,
                order="date",
                type="video",
                safeSearch="none",
                videoDuration="any",
                regionCode="RU",
                part="id, snippet",
                maxResults=max_results,
                pageToken=page_token
            ).execute()
        except HttpError as err:
            if err.status_code == 403 and err.reason == YoutubeApiClient.QUOTA_REASON:
                # TODO LOGGING
                print("Quota exceeded")

            search_response = {}
        next_page_token: str = search_response.get("nextPageToken", "")
        prev_page_token: str = search_response.get("prevPageToken", "")
        entities: list = search_response.get("items", [])
        dtos: list[VideoDTO] = []
        for entity in entities:
            dtos.append(YoutubeMapper.to_dto(entity))

        return YoutubeDTO(
            next_page_token=next_page_token,
            prev_page_token=prev_page_token,
            entities=dtos
        )
