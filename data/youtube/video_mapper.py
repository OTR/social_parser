""""""
import os
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

from dotenv import load_dotenv

from app.models.content import ContentModel
from data.youtube.video_dto import VideoDTO
from domain.entity.youtube_video import YoutubeVideo

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "python_anywhere.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)


class VideoMapper:
    """"""
    _iso_datetime_format: str = "%Y-%m-%dT%H:%M:%SZ"
    _readable_datetime_format: str = "%Y.%m.%d %H:%M:%S"
    _offset = int(os.getenv("TIMEZONE_OFFSET"))

    @staticmethod
    def datetime_to_local_datetime(utc_datetime: datetime) -> datetime:
        """"""
        return utc_datetime + timedelta(hours=VideoMapper._offset)

    @staticmethod
    def get_readable_datetime(date_time: datetime) -> str:
        return datetime.strftime(date_time, VideoMapper._readable_datetime_format)

    @staticmethod
    def json_to_dto(entity: dict) -> VideoDTO:
        """"""
        title: str = entity["snippet"]["title"]
        channel_title: str = entity["snippet"]["channelTitle"]
        channel_id: str = entity["snippet"]["channelId"]
        video_id: str = entity["id"]["videoId"]
        description: str = entity['snippet']['description']
        thumbnail_url: str = entity['snippet']['thumbnails']['default']['url']

        _published_at: str = entity["snippet"]["publishedAt"]
        published_at: datetime = datetime.strptime(_published_at, VideoMapper._iso_datetime_format)
        published_at_with_tz = VideoMapper.datetime_to_local_datetime(published_at)

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
    def entity_to_text(entity: YoutubeVideo) -> str:
        """"""
        title = entity.title
        _published_at = entity.published_at
        local_published_at: datetime = VideoMapper.datetime_to_local_datetime(_published_at)
        readable_published_at: str = VideoMapper.get_readable_datetime(local_published_at)
        channel_title = entity.channel_title
        youtube_url = entity.get_video_url()
        return f"{title}\n{channel_title}\n{readable_published_at}\n{youtube_url}\n"

    @staticmethod
    def dto_to_entity(dto: VideoDTO) -> YoutubeVideo:
        """"""
        title: str = dto.title
        channel_id: str = dto.channel_id
        published_at: datetime = dto.published_at
        channel_title: str = dto.channel_title
        video_id: str = dto.video_id
        description: str = dto.description

        return YoutubeVideo(
            title=title,
            published_at=published_at,
            channel_id=channel_id,
            channel_title=channel_title,
            video_id=video_id,
            description=description
        )


    @staticmethod
    def dbo_to_entity(dbo: ContentModel) -> YoutubeVideo:
        """"""
        title: str = dbo.title
        channel_id: str = ""  # TODO: Remove
        published_at: datetime = dbo.published_at
        channel_title: str = dbo.username
        video_id: str = dbo.content_id
        description: str = ""  # TODO: Remove

        return YoutubeVideo(
            title=title,
            published_at=published_at,
            channel_id=channel_id,
            channel_title=channel_title,
            video_id=video_id,
            description=description
        )
