""""""
from dataclasses import dataclass

from service.youtube.video_dto import VideoDTO


@dataclass
class YoutubeDTO:
    """
    next_page_token - youtube requires for accessing next entities from offset
    prev_page_token
    entities
    """
    next_page_token: str
    prev_page_token: str
    entities: list[VideoDTO]
