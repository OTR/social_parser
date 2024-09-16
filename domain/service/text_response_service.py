""""""
import os
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Optional, List

import pytz
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / "python_anywhere.env")
DEFAULT_DJANGO_SETTINGS = os.getenv("DEFAULT_DJANGO_SETTINGS")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_DJANGO_SETTINGS)
import django
django.setup()


from app.templatetags.custom_filters import time_since
from data.youtube.dto.channel_details_dto import ChannelDetailsDTO
from data.youtube.mapper.video_mapper import VideoMapper
from domain.entity.youtube_video import YoutubeVideo


class TextResponseService:

    @staticmethod
    def combine_video_channel_reply(videos: list[YoutubeVideo], channels: list[ChannelDetailsDTO]) -> str:
        """"""
        response: str = ""
        for entity in videos:
            title = entity.title
            _published_at = entity.published_at
            local_timezone = pytz.timezone('Etc/GMT-' + str(VideoMapper._TIMEZONE_OFFSET))
            local_published_at: datetime = _published_at.astimezone(local_timezone)
            readable_published_at: str = VideoMapper.get_readable_datetime(local_published_at)
            channel_title = entity.channel_title
            youtube_url = entity.get_video_url()
            local_time_since = time_since(local_published_at)

            channel_id: str = entity.channel_id
            channel: ChannelDetailsDTO = TextResponseService.find_channel_by_id(channels, channel_id)
            subscribers = channel.subscribers_count if channel else ""
            country = channel.country if channel else ""
            channel_description = channel.description if channel else ""

            response += textwrap.dedent(f"""
                Video title: {title}
                Channel name: {channel_title}
                Channel description: {channel_description}
                Subscribers: {subscribers}
                Country: {country}
                Published at: {readable_published_at}
                {local_time_since}
                {youtube_url}""").strip() + "\n\n"

        return response

    @staticmethod
    def find_channel_by_id(channels: List[ChannelDetailsDTO], channel_id: str) -> Optional[
        ChannelDetailsDTO]:
        """
        Filters and returns the entity from the list with the given channel_id.
        If no match is found, returns None.

        Args:
            channels (List[ChannelDetailsDTO]): The list of channel entities.
            channel_id (str): The channel ID to search for.

        Returns:
            Optional[ChannelDetailsDTO]: The matching entity or None if not found.
        """
        return next((channel for channel in channels if channel.channel_id == channel_id), None)
