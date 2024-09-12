from abc import abstractmethod


class BaseSocialParserException(Exception):
    """"""

    @abstractmethod
    def get_reason(self) -> str:
        """"""
