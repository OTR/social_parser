""""""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ChannelDetailsDTO:
    """"""
    channel_id: str
    title: str
    description: str
    custom_url: str
    created_at: datetime
    country: str
    view_count: int
    subscribers_count: int
    video_count: int
    topic_categories: list[str]
    keywords: str
