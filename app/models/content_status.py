""""""
from enum import Enum


class ContentStatus(Enum):
    """"""
    IN_PROGRESS: str = "IN PROGRESS"
    TO_DO: str = "TO DO"
    DONE: str = "DONE"
    REJECTED: str = "REJECTED"
    NOT_LABELED: str = "NOT LABELED"
