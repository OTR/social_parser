from repository.base_youtube_repository import BaseYoutubeRepository
from domain.entity.youtube_video import YoutubeVideo
from data.youtube.video_mapper import VideoMapper
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")

import django
django.setup()

from app.models.content import ContentModel


class InternalYoutubeRepository(BaseYoutubeRepository):
    """"""

    def get_videos(self) -> list[YoutubeVideo]:
        """"""

    def get_all_videos(self) -> list[YoutubeVideo]:
        dbos = ContentModel.objects.all()

        return dbos
