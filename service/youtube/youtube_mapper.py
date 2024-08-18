""""""
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

from service.youtube.video_dto import VideoDTO

load_dotenv()


class YoutubeMapper:
    """"""

    @staticmethod
    def to_dto(entity: dict) -> VideoDTO:
        """"""
        offset = int(os.getenv("TIMEZONE_OFFSET"))
        _datetime_format: str = "%Y-%m-%dT%H:%M:%SZ"

        title: str = entity["snippet"]["title"]
        channel_title: str = entity["snippet"]["channelTitle"]
        channel_id: str = entity["snippet"]["channelId"]
        video_id: str = entity["id"]["videoId"]
        description: str = entity['snippet']['description']
        thumbnail_url: str = entity['snippet']['thumbnails']['default']['url']

        _published_at: str = entity["snippet"]["publishedAt"]
        published_at: datetime = datetime.strptime(_published_at, _datetime_format)
        published_at_with_tz = published_at + timedelta(hours=offset)

        return VideoDTO(
            title=title,
            published_at=published_at_with_tz,
            channel_id=channel_id,
            channel_title=channel_title,
            video_id=video_id,
            description=description,
            thumbnail_url=thumbnail_url
        )
