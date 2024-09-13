import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")

import django
django.setup()

from app.models.highlight import HighlightModel
from data.youtube.mapper.channel_mapper import ChannelMapper
from domain.entity.youtube_channel import YoutubeChannel


class InternalHighlightRepository:
    """"""

    def get_highlighters(self) -> list[YoutubeChannel]:
        """"""
        dbos: list[HighlightModel] = HighlightModel.objects.filter()
        entities: list[YoutubeChannel] = list(map(ChannelMapper.dbo_to_entity, dbos))

        return entities

    def get_blocked_channel_ids(self) -> list[int]:
        """"""
        blocked_channel_ids: list[int] = HighlightModel.objects.values_list('channel_id', flat=True)
        return blocked_channel_ids
