""""""
from dataclasses import dataclass


@dataclass
class HighlighterDTO:
    """
    channel_id
    channel_title
    reason
    """
    channel_id: str
    channel_title: str
    reason: str

    def get_fields_as_dict(self) -> dict:
        """"""
        return {
            "channel_id": self.channel_id,
            "channel_title": self.channel_title,
            "reason": self.reason
        }
