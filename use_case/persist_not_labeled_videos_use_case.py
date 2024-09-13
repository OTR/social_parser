""""""
from domain.entity.youtube_video import YoutubeVideo
from domain.vo.content_status import ContentStatus
from repository.youtube.internal_youtube_repository import InternalYoutubeRepository


class PersistNotLabeledVideosUseCase:
    """"""

    def __init__(
        self,
        internal_youtube_repository = InternalYoutubeRepository()
    ):
        """"""
        self._youtube_repo = internal_youtube_repository

    def execute(self, videos_to_persist: list[YoutubeVideo]) -> None:
        """"""
        self._youtube_repo.persist_all_videos(videos_to_persist, ContentStatus.NOT_LABELED)
