""""""
from domain.entity.youtube_video import YoutubeVideo
from repository.youtube.internal_highlight_repository import InternalHighlightRepository
from repository.youtube.internal_youtube_repository import InternalYoutubeRepository


class FilterHighlightersAndKnownVideosUseCase:
    """"""

    def __init__(
        self,
        content_repository = InternalYoutubeRepository(),
        highlight_repository = InternalHighlightRepository()
    ):
        """"""
        self._content_repository = content_repository
        self._highlight_repository = highlight_repository

    def execute(self, videos_to_filter: list[YoutubeVideo]) -> list[YoutubeVideo]:
        """"""
        blocked_channel_ids: list[int] = self._highlight_repository.get_blocked_channel_ids()
        known_videos_ids: list[int] = self._content_repository.get_all_videos_ids()
        filtered_videos: list[YoutubeVideo] = [
            video for video in videos_to_filter
            if video.channel_id not in blocked_channel_ids
               and video.video_id not in known_videos_ids
        ]

        return filtered_videos
