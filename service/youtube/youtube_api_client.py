""""""
import os
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build

from service.youtube.youtube_dto import YoutubeDTO
from service.youtube.video_dto import VideoDTO
from service.youtube.youtube_mapper import YoutubeMapper

load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")


class YoutubeApiClient:
    """"""

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

        next_page_token: str = search_response.get("nextPageToken")
        entities: list = search_response.get("items", [])
        dtos: list[VideoDTO] = []
        for entity in entities:
            dtos.append(YoutubeMapper.to_dto(entity))

        return YoutubeDTO(
            next_page_token=next_page_token,
            entities=dtos
        )
