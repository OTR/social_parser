""""""
from datetime import datetime, timedelta
import os

from service.youtube.comment_dto import CommentDTO


class CommentMapper:
    """"""

    @staticmethod
    def to_dto(entity: dict) -> CommentDTO:
        """"""
        offset = int(os.getenv("TIMEZONE_OFFSET"))
        _datetime_format: str = "%Y-%m-%dT%H:%M:%SZ"

        comment_id: str = entity["id"]
        channel_id: str = entity["snippet"]["channelId"]
        video_id: str = entity["snippet"]["videoId"]
        text_original: str = entity["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        author_name: str = entity["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        author_channel_url: str = entity["snippet"]["topLevelComment"]["snippet"]["authorChannelUrl"]
        like_count: int = int(entity["snippet"]["topLevelComment"]["snippet"]["likeCount"])

        _published_at: str = entity["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
        published_at: datetime = datetime.strptime(_published_at, _datetime_format)
        published_at_with_tz = published_at + timedelta(hours=offset)

        return CommentDTO(
            comment_id=comment_id,
            channel_id=channel_id,
            video_id=video_id,
            text=text_original,
            comment_author_name=author_name,
            comment_author_channel_url=author_channel_url,
            like_count=like_count,
            published_at=published_at_with_tz
        )

