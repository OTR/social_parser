from repository.base_youtube_repository import BaseYoutubeRepository
from domain.entity.youtube_video import YoutubeVideo


class ExternalYoutubeRepository(BaseYoutubeRepository):
    """"""

    def get_videos(self) -> list[YoutubeVideo]:
        pass


