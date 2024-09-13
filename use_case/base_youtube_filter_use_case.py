from abc import ABC, abstractmethod

from domain.entity.youtube_video import YoutubeVideo


class BaseYoutubeFilterUseCase(ABC):
    """"""

    @abstractmethod
    def execute(self, videos_to_filter: list[YoutubeVideo]) -> list[YoutubeVideo]:
        """"""
