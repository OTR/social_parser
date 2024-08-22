from domain.entity.youtube_video import YoutubeVideo
from use_case.base_youtube_use_case import BaseYoutubeUseCase
from data.youtube.youtube_api_client import YoutubeApiClient


class GetAnyYoutubeVideosUseCase(BaseYoutubeUseCase):
    """"""

    def __init__(self):
        self.youtube_api_client = YoutubeApiClient()

    def get_videos(self) -> list[YoutubeVideo]:
        self.youtube_api_client.get_latest_videos(duration="any")
