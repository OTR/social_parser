""""""
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv

from app.models.content import ContentModel
from data.youtube.video_dto import VideoDTO
from domain.entity.youtube_video import YoutubeVideo

load_dotenv()


class VideoMapper:
    """"""

    @staticmethod
    def json_to_dto(entity: dict) -> VideoDTO:
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

    @staticmethod
    def dto_to_text(dto: VideoDTO) -> str:
        """"""
        title = dto.title
        published_at = dto.published_at
        channel_title = dto.channel_title
        video_id = dto.video_id
        youtube_url = "https://youtube.com/watch=v?" + str(video_id)
        return f"{title}\n{channel_title}\n{youtube_url}\n"

    @staticmethod
    def dbo_to_entity(dbo: ContentModel) -> YoutubeVideo:
        """"""
        title = dbo.title
        published_at: datetime = None
        channel_id: str = None
        channel_title: str = None
        video_id: str = None
        description: str = None

        return YoutubeVideo(
            title="",
            published_at=datetime.now(),
            channel_id=",",
            channel_title="",
            video_id="",
            description=""
        )
