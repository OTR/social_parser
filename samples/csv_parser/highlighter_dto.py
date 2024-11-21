from dataclasses import dataclass


@dataclass
class HighlighterDTO:
    """
    Represents a data transfer object (DTO) for a highlighter channel.

    - `channel_id`: (str) YouTube native channel ID.
    - `channel_title`: (str) The title of the channel.
    - `reason`: (str) The reason for being marked as a highlighter.

    The `get_fields_as_dict()` method returns a dict representation of the DTO.
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
