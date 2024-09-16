import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()

from data.youtube.dto.channel_details_dto import ChannelDetailsDTO
from domain.entity.youtube_video import YoutubeVideo
from use_case.acquire_channel_details_use_case import AcquireChannelDetailsUseCase
from use_case.get_long_youtube_videos_use_case import GetLongYoutubeVideosUseCase
from use_case.get_any_youtube_videos_use_case import GetAnyYoutubeVideosUseCase
from use_case.get_medium_youtube_videos_use_case import GetMediumYoutubeVideosUseCase
from use_case.filter_known_videos_use_case import FilterHighlightersAndKnownVideosUseCase
from use_case.persist_not_labeled_videos_use_case import PersistNotLabeledVideosUseCase


class YoutubeVideoService:
    """"""

    def __init__(
            self,
            any_videos_use_case = GetAnyYoutubeVideosUseCase(),
            medium_videos_use_case = GetMediumYoutubeVideosUseCase(),
            long_videos_use_case = GetLongYoutubeVideosUseCase(),
            filter_known_videos_use_case = FilterHighlightersAndKnownVideosUseCase(),
            persist_videos_use_case = PersistNotLabeledVideosUseCase(),
            acquire_channel_details_use_case = AcquireChannelDetailsUseCase()
    ):
        """"""
        self._get_any_youtube_videos_use_case = any_videos_use_case
        self._get_medium_youtube_videos_use_case = medium_videos_use_case
        self._get_long_youtube_videos_use_case = long_videos_use_case
        self._filter_known_videos_use_case = filter_known_videos_use_case
        self._persist_not_labeled_videos_use_case = persist_videos_use_case
        self._acquire_channel_details_use_case = acquire_channel_details_use_case

    def get_and_persist_not_labeled_youtube_videos(self):
        """
        1. Get the newest videos only with medium and lange duration
        2. filter out already known videos and videos from Highlighter channels
        3. For those who left make additional API request and update entities with channel info
        """
        medium_youtube_videos: list[YoutubeVideo] = self._get_medium_youtube_videos_use_case.execute()
        long_youtube_videos: list[YoutubeVideo] = self._get_long_youtube_videos_use_case.execute()
        youtube_videos = list(set(medium_youtube_videos) | set(long_youtube_videos))
        filtered_videos: list[YoutubeVideo] = self._filter_known_videos_use_case.execute(youtube_videos)
        self._persist_not_labeled_videos_use_case.execute(filtered_videos)

        return filtered_videos

    def get_channel_details(self, videos: list[YoutubeVideo]) -> list[ChannelDetailsDTO]:
        """"""
        channel_details = self._acquire_channel_details_use_case.execute(videos)
        return channel_details

    def get_any_untracked_youtube_videos(self) -> list[YoutubeVideo]:
        """"""
        youtube_videos: list[YoutubeVideo] = self._get_any_youtube_videos_use_case.execute()
        filtered_videos: list[YoutubeVideo] = self._filter_known_videos_use_case.execute(youtube_videos)

        return filtered_videos
