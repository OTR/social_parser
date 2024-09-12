import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test_settings")

import django
django.setup()

from app.models.highlight import HighlightModel
from domain.entity.youtube_channel import YoutubeChannel
from data.youtube.channel_mapper import ChannelMapper


class InternalHighlightRepository:
    """"""

    def get_highlighters(self):
        """"""
        dbos: list[HighlightModel] = HighlightModel.objects.filter()
        entities: list[YoutubeChannel] = list(map(ChannelMapper.dbo_to_entity, dbos))

        return entities
