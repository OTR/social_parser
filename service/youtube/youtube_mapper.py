""""""
from service.youtube import VideoDTO
from datetime import datetime


class YoutubeMapper:
    """"""

    @staticmethod
    def to_dto(entity: dict) -> VideoDTO:
        """"""
        title: str = entity["snippet"]["title"]
        _published_at: str = entity["snippet"]["publishedAt"]
        _datetime_format: str = "%Y-%m-%dT%H:%M:%SZ"
        published_datetime: datetime = datetime.strptime(_published_at, _datetime_format)
        channel_title: str = entity["snippet"]["channelTitle"]
        channel_id: str = entity["snippet"]["channelId"]
        video_id: str = entity["id"]["videoId"]
        description: str = entity['snippet']['description']
        thumbnail_url: str = entity['snippet']['thumbnails']['default']['url']

        return VideoDTO(
            title=title,
            published_datetime=published_datetime,
            channel_id=channel_id,
            channel_title=channel_title,
            video_id=video_id,
            description=description,
            thumbnail_url=thumbnail_url
        )
