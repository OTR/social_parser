from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class YoutubeChannel:
    """
    Represents a YouTube channel.
    Attributes:
        channel_id (str): The unique identifier for the YouTube channel.
        channel_title (str): The title or name of the YouTube channel.
    """
    channel_id: str
    channel_title: str
