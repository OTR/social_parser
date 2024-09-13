from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, eq=True)
class YoutubeVideo:
    """
     A class to represent a YouTube video.

     Attributes:
         title (str): The title of the YouTube video.
         published_at (datetime): The date and time when the video was published.
         channel_id (str): The unique identifier for the YouTube channel.
         channel_title (str): The title or name of the YouTube channel.
         video_id (str): The unique identifier for the YouTube video.
         description (str): The description provided for the YouTube video.

     Methods:
     --------
     get_video_url() -> str: Returns the full URL to the YouTube video.
     """
    title: str
    published_at: datetime
    channel_id: str
    channel_title: str
    video_id: str
    description: str

    def get_video_url(self):
        """"""
        return "https://youtube.com/watch?v=" + str(self.video_id)
