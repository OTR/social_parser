from dataclasses import dataclass
from datetime import datetime


@dataclass
class YoutubeVideo:
    """"""
    title: str
    published_at: datetime
    channel_id: str
    channel_title: str
    video_id: str
    description: str

    def get_video_url(self):
        """"""
        return "https://youtube.com/watch?v=" + str(self.video_id)
