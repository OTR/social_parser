""""""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CommentDTO:
    """"""
    comment_id: str
    channel_id: str
    video_id: str
    text: str
    comment_author_name: str
    comment_author_channel_url: str
    like_count: int
    published_at: datetime
