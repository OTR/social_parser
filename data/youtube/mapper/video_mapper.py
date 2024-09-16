""""""
import os
import textwrap
from pathlib import Path
from datetime import datetime, timedelta, timezone

import pytz
from dotenv import load_dotenv

from app.models.content import ContentModel
from app.templatetags.custom_filters import time_since
from data.youtube.dto.video_dto import VideoDTO
from domain.entity.youtube_video import YoutubeVideo
from domain.vo.content_platform import ContentPlatform
from domain.vo.content_status import ContentStatus

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent.parent / "python_anywhere.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)


class VideoMapper:
    """Mapper class to convert between different representations of video data."""
    _ISO_DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%SZ"
    _READABLE_DATETIME_FORMAT: str = "%d.%m.%Y %H:%M:%S"
    _TIMEZONE_OFFSET: int = int(os.getenv("TIMEZONE_OFFSET"))
    __NOT_DEFINED_INT = -1
    __NOT_DEFINED_BOOL = False
    __DBO_REASON_FOR_AUTO_CONVERT = "Quickly added as not labeled by telegram notificator"

    @staticmethod
    def datetime_to_local_datetime(utc_datetime: datetime) -> datetime:
        """Deprecated"""
        return utc_datetime + timedelta(hours=VideoMapper._TIMEZONE_OFFSET)

    @staticmethod
    def get_readable_datetime(date_time: datetime) -> str:
        """"""
        return datetime.strftime(date_time, VideoMapper._READABLE_DATETIME_FORMAT)

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
        published_at: datetime = datetime.strptime(_published_at, VideoMapper._ISO_DATETIME_FORMAT)
        published_at_with_tz = published_at.replace(tzinfo=pytz.UTC)

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
        local_timezone = pytz.timezone('Etc/GMT-' + str(VideoMapper._TIMEZONE_OFFSET))
        local_published_at: datetime = _published_at.astimezone(local_timezone)
        readable_published_at: str = VideoMapper.get_readable_datetime(local_published_at)
        channel_title = entity.channel_title
        youtube_url = entity.get_video_url()
        local_time_since = time_since(local_published_at)
        return textwrap.dedent(f"""
            {title}
            {channel_title}
            {readable_published_at}
            {local_time_since}
            {youtube_url}""").strip()

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

    @staticmethod
    def entity_to_dbo(
        entity: YoutubeVideo,
        content_status: ContentStatus = ContentStatus.NOT_LABELED
    ) -> ContentModel:
        """
        Converts a `YoutubeVideo` domain entity to a `ContentModel` database object.
        For fields that absent in `YoutubeVideo` domain entity assert placeholders
        that are obviously not existing values like -1 for integer
        Args:
            entity (YoutubeVideo): The YoutubeVideo entity to convert.
            content_status (ContentStatus): moderation status of the video, default `NOT_LABELED`
        Returns:
            ContentModel: The corresponding ContentModel instance.
        """
        timezone_aware_datetime: datetime = entity.published_at.replace(
            tzinfo=timezone(timedelta(hours=VideoMapper._TIMEZONE_OFFSET))
        )

        dbo = ContentModel(
            username=entity.channel_title,
            subscribers=VideoMapper.__NOT_DEFINED_INT,
            platform=ContentPlatform.YOUTUBE.value,
            content_id=entity.video_id,
            link=entity.get_video_url(),
            seized_top=VideoMapper.__NOT_DEFINED_BOOL,
            # Default values for fields not present in YoutubeVideo entity
            # Assuming some fields like subscribers, views, likes, etc. are not part of YoutubeVideo
            views=VideoMapper.__NOT_DEFINED_INT,
            likes=VideoMapper.__NOT_DEFINED_INT,
            shares=VideoMapper.__NOT_DEFINED_INT,
            comments=VideoMapper.__NOT_DEFINED_INT,
            published_at=timezone_aware_datetime,
            title=entity.title,
            reason=VideoMapper.__DBO_REASON_FOR_AUTO_CONVERT,
            through_suggestion=VideoMapper.__NOT_DEFINED_BOOL,
            status=content_status.value,
        )
        return dbo
