from abc import ABC, abstractmethod
from domain.entity.youtube_video import YoutubeVideo


class BaseYoutubeRepository(ABC):
    """"""

    @abstractmethod
    def get_videos(self) -> list[YoutubeVideo]:
        """"""
