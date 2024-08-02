""""""
from dataclasses import dataclass

from service.youtube import VideoDTO


@dataclass
class YoutubeDTO:
    """
    next_page_token - youtube requires for accessing next entities from offset
    entities
    """
    next_page_token: str
    entities: list[VideoDTO]
