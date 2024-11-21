from dataclasses import dataclass


@dataclass
class TargetDTO:
    _number: int
    username: str
    title: str
    subscribers: int
    link: str
    platform: str
    content_id: str
    seized_top: bool
    views: int
    likes: int
    shares: int
    comments: int
    published_at: str
    reason: str
    status: str
    through_suggestion: bool

    def get_fields_as_dict(self) -> dict:
        return {
            "username": self.username,
            "subscribers": self.subscribers,
            "platform": self.platform,
            "content_id": self.content_id,
            "link": self.link,
            "seized_top": self.seized_top,
            "views": self.views,
            "likes": self.likes,
            "shares": self.shares,
            "comments": self.comments,
            "published_at": self.published_at,
            "title": self.title,
            "reason": self.reason,
            "through_suggestion": self.through_suggestion,
            "status": self.status
        }
