import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()

from app.models import HighlightModel, ContentModel
from domain.entity.youtube_video import YoutubeVideo
from domain.vo.content_platform import ContentPlatform
from use_case.get_long_youtube_videos_use_case import GetLongYoutubeVideosUseCase
from use_case.get_any_youtube_videos_use_case import GetAnyYoutubeVideosUseCase
from use_case.get_medium_youtube_videos_use_case import GetMediumYoutubeVideosUseCase


class YoutubeVideoService:
    """"""

    def __init__(
            self,
            any_videos_use_case = GetAnyYoutubeVideosUseCase(),
            medium_videos_use_case = GetMediumYoutubeVideosUseCase(),
            long_videos_use_case = GetLongYoutubeVideosUseCase()
    ):
        """"""
        self._get_any_youtube_videos_use_case = any_videos_use_case
        self._get_medium_youtube_videos_use_case = medium_videos_use_case
        self._get_long_youtube_videos_use_case = long_videos_use_case

    def get_untracked_youtube_videos(self):
        """"""

    def get_not_labeled_youtube_videos(self) -> list[YoutubeVideo]:
        """"""
        youtube_dto = self._get_any_youtube_videos_use_case.get_videos()
        blocked_channels = HighlightModel.objects.values_list('channel_id', flat=True)
        existing_content_ids = (ContentModel.objects
                                .filter(platform=ContentPlatform.YOUTUBE.value)
                                .values_list('content_id', flat=True))
        filtered_videos = [
            video for video in youtube_dto
            if video.channel_id not in blocked_channels
               and video.video_id not in existing_content_ids
        ]

        return filtered_videos
