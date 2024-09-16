from data.youtube.dto.channel_details_dto import ChannelDetailsDTO
from data.youtube.youtube_api_client import YoutubeApiClient
from data.youtube.mapper.video_mapper import VideoMapper
from domain.entity.youtube_video import YoutubeVideo
from use_case.base_youtube_filter_use_case import BaseYoutubeFilterUseCase


class AcquireChannelDetailsUseCase:
    """"""

    def __init__(
        self,
        youtube_api_client=YoutubeApiClient()
    ):
        """"""
        self._client = youtube_api_client

    def execute(self, videos_to_filter: list[YoutubeVideo]) -> list[ChannelDetailsDTO]:
        """"""
        channel_ids: list[str] = list(map(lambda x: x.channel_id, videos_to_filter))
        dtos: list[ChannelDetailsDTO] = self._client.get_channel_statistics(channel_ids=channel_ids)

        return dtos
