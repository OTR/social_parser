from data.youtube.mapper.video_mapper import VideoMapper
from data.youtube.youtube_api_client import YoutubeApiClient
from domain.entity.youtube_video import YoutubeVideo
from use_case.base_youtube_use_case import BaseYoutubeUseCase


class GetLongYoutubeVideosUseCase(BaseYoutubeUseCase):
    """"""

    def __init__(
        self,
        youtube_api_client=YoutubeApiClient()
    ):
        self._youtube_api_client = youtube_api_client

    def execute(self) -> list[YoutubeVideo]:
        youtube_dto = self._youtube_api_client.get_latest_videos(duration="long")
        youtube_videos = list(map(VideoMapper.dto_to_entity, youtube_dto.entities))
        return youtube_videos
