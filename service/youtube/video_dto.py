""""""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class VideoDTO:
    """"""
    title: str
    published_at: datetime
    channel_id: str
    channel_title: str
    video_id: str
    description: str
    thumbnail_url: str

    @property
    def strftime(self):
        return "GG"
