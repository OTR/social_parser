import os
from pathlib import Path
from dotenv import load_dotenv

from use_case.persist_not_labeled_videos_use_case import PersistNotLabeledVideosUseCase

load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()

from domain.entity.youtube_video import YoutubeVideo
from use_case.get_long_youtube_videos_use_case import GetLongYoutubeVideosUseCase
from use_case.get_any_youtube_videos_use_case import GetAnyYoutubeVideosUseCase
from use_case.get_medium_youtube_videos_use_case import GetMediumYoutubeVideosUseCase
from use_case.filter_known_videos_use_case import FilterHighlightersAndKnownVideosUseCase


class YoutubeVideoService:
    """"""

    def __init__(
            self,
            any_videos_use_case = GetAnyYoutubeVideosUseCase(),
            medium_videos_use_case = GetMediumYoutubeVideosUseCase(),
            long_videos_use_case = GetLongYoutubeVideosUseCase(),
            filter_known_videos_use_case = FilterHighlightersAndKnownVideosUseCase(),
            persist_videos_use_case = PersistNotLabeledVideosUseCase()
    ):
        """"""
        self._get_any_youtube_videos_use_case = any_videos_use_case
        self._get_medium_youtube_videos_use_case = medium_videos_use_case
        self._get_long_youtube_videos_use_case = long_videos_use_case
        self._filter_known_videos_use_case = filter_known_videos_use_case
        self._persist_not_labeled_videos_use_case = persist_videos_use_case

    def get_and_persist_not_labeled_youtube_videos(self):
        """"""
        # any_youtube_videos: list[YoutubeVideo] = self._get_any_youtube_videos_use_case.execute()
        medium_youtube_videos: list[YoutubeVideo] = self._get_medium_youtube_videos_use_case.execute()
        long_youtube_videos: list[YoutubeVideo] = self._get_long_youtube_videos_use_case.execute()
        youtube_videos = list(set(medium_youtube_videos) | set(long_youtube_videos))
        filtered_videos: list[YoutubeVideo] = self._filter_known_videos_use_case.execute(youtube_videos)
        self._persist_not_labeled_videos_use_case.execute(filtered_videos)

        return filtered_videos

    def get_any_untracked_youtube_videos(self) -> list[YoutubeVideo]:
        """"""
        youtube_videos: list[YoutubeVideo] = self._get_any_youtube_videos_use_case.execute()
        filtered_videos: list[YoutubeVideo] = self._filter_known_videos_use_case.execute(youtube_videos)

        return filtered_videos


if __name__ == '__main__':
    service = YoutubeVideoService()

