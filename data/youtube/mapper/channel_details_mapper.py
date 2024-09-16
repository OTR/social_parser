""""""
import re
from datetime import datetime

import pytz

from data.youtube.dto.channel_details_dto import ChannelDetailsDTO


class ChannelDetailsMapper:
    """"""
    _ISO_DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%SZ"
    _ISO_FRACTIONAL_DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S.%fZ"

    @staticmethod
    def json_to_dto(entity: dict) -> ChannelDetailsDTO:
        """"""
        channel_id: str = entity["id"]
        title: str = entity["snippet"]["title"]
        description: str = entity["snippet"]["description"]
        custom_url: str = entity["snippet"]["customUrl"]
        _created_at: str = entity["snippet"]["publishedAt"]
        country: str = entity["snippet"].get("country", "Unknown")
        view_count: int = int(entity["statistics"]["viewCount"])
        subscribers_count: int = int(entity["statistics"]["subscriberCount"])
        video_count: int = int(entity["statistics"]["videoCount"])
        _topic_categories: list[str] = entity["topicDetails"]["topicCategories"] if entity.get("topicDetails", None) else [""]
        topic_categories: list[str] = list(map(lambda x: x.split("/")[-1], _topic_categories))
        keywords: str = entity["brandingSettings"]["channel"]["keywords"] if entity["brandingSettings"]["channel"].get("keywords", None) else ""

        if re.search(r"\.\d+Z$", _created_at):
            fmt = ChannelDetailsMapper._ISO_FRACTIONAL_DATETIME_FORMAT
        else:
            fmt = ChannelDetailsMapper._ISO_DATETIME_FORMAT

        created_at: datetime = datetime.strptime(_created_at, fmt)
        created_at_with_tz = created_at.replace(tzinfo=pytz.UTC)

        return ChannelDetailsDTO(
            channel_id=channel_id,
            title=title,
            description=description,
            custom_url=custom_url,
            created_at=created_at_with_tz,
            country=country,
            view_count=view_count,
            subscribers_count=subscribers_count,
            video_count=video_count,
            topic_categories=topic_categories,
            keywords=keywords
        )
