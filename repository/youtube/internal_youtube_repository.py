import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")

import django
django.setup()

from app.models.content import ContentModel
from data.youtube.video_mapper import VideoMapper
from domain.entity.youtube_video import YoutubeVideo
from domain.vo.content_platform import ContentPlatform
from repository.base_youtube_repository import BaseYoutubeRepository


class InternalYoutubeRepository(BaseYoutubeRepository):
    """"""

    def get_videos(self) -> list[YoutubeVideo]:
        """"""

    def get_all_videos(self) -> list[YoutubeVideo]:
        dbos: list[ContentModel] = ContentModel.objects.filter(
            platform=ContentPlatform.YOUTUBE.value
        )
        entities: list[YoutubeVideo] = list(map(VideoMapper.dbo_to_entity, dbos))

        return entities
