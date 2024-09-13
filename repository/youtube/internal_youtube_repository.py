import os
from logging import Logger

from data.file_logger import FileLogger
from domain.vo.content_status import ContentStatus

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")

import django
django.setup()

from app.models.content import ContentModel
from data.youtube.mapper.video_mapper import VideoMapper
from domain.entity.youtube_video import YoutubeVideo
from domain.vo.content_platform import ContentPlatform
from repository.base_youtube_repository import BaseYoutubeRepository


class InternalYoutubeRepository(BaseYoutubeRepository):
    """"""

    def __init__(self):
        """"""
        self._logger: Logger = FileLogger().get_logger()

    def get_videos(self) -> list[YoutubeVideo]:
        """"""

    def get_all_videos(self) -> list[YoutubeVideo]:
        """"""
        dbos: list[ContentModel] = ContentModel.objects.filter(
            platform=ContentPlatform.YOUTUBE.value
        )
        entities: list[YoutubeVideo] = list(map(VideoMapper.dbo_to_entity, dbos))

        return entities

    def get_all_videos_ids(self) -> list[int]:
        """"""
        all_videos_ids: list[int] = (ContentModel.objects
                                    .filter(platform=ContentPlatform.YOUTUBE.value)
                                    .values_list('content_id', flat=True))

        return all_videos_ids

    def persist_all_videos(
            self,
            entities_to_persist: list[YoutubeVideo],
            content_status: ContentStatus = ContentStatus.NOT_LABELED
    ) -> None:
        """"""
        try:
            dbos: list[ContentModel] = list(
                map(
                    lambda x: VideoMapper.entity_to_dbo(x, content_status),
                    entities_to_persist
                )
            )
            ContentModel.objects.bulk_create(dbos)
        except Exception as err:
            self._logger.debug(f"Could not persist DB owner {err}")
            raise err
