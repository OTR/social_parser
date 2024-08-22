from exception.base_social_parser_exception import BaseSocialParserException


class YoutubeApiQuotaExceeded(BaseSocialParserException):
    """"""
    _DEFAULT_REASON = "Youtube API Quota exceeded for key: "

    def __init__(self, api_key: str):
        """"""
        self._api_key = api_key

    def get_reason(self) -> str:
        """"""
        return self._DEFAULT_REASON + self._api_key
