""""""
from enum import Enum


class ContentStatus(Enum):
    """"""
    IN_PROGRESS: str = "IN PROGRESS"
    TO_DO: str = "TO DO"
    DONE: str = "DONE"
    REJECTED: str = "REJECTED"
    NOT_LABELED: str = "NOT LABELED"

    def as_uri(self):
        """"""
        return self.value.lower().replace(" ", "_")

    @staticmethod
    def all_uri_params():
        """"""
        return ["in_progress", "to_do", "done", "rejected", "not_labeled"]

