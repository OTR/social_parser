from exception.base_social_parser_exception import BaseSocialParserException


class YoutubeNoAvailableKeysToRotateTo(BaseSocialParserException):
    """"""
    _DEFAULT_REASON = "No available API keys to rotate to."

    def __init__(self, api_key: str):
        """"""
        self._api_key = api_key

    def get_reason(self) -> str:
        """"""
        return self._DEFAULT_REASON + self._api_key
