""""""
from app.models.highlight import HighlightModel
from domain.entity.youtube_channel import YoutubeChannel


class ChannelMapper:
    """"""

    @staticmethod
    def dbo_to_entity(dbo: HighlightModel) -> YoutubeChannel:
        """"""
        channel_id: str = dbo.channel_id
        channel_title: str = dbo.channel_title

        return YoutubeChannel(
            channel_id=channel_id,
            channel_title=channel_title
        )
