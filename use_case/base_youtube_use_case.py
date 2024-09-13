from abc import ABC, abstractmethod

from domain.entity.youtube_video import YoutubeVideo


class BaseYoutubeUseCase(ABC):
    """"""

    @abstractmethod
    def execute(self) -> list[YoutubeVideo]:
        """"""
