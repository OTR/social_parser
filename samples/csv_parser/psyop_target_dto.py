""""""
from dataclasses import dataclass


@dataclass
class PsyOpTargetDTO:
    number: int
    username: str
    subscribers: int
    link: str
    platform: str
    content_id: str
    seized_top: bool
    views: int
    likes: int
    shares: int
    comments: str
    added_date: str
    reason: str
    status: str
    through_suggestion: bool
