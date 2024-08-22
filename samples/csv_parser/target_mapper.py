""""""
from typing import Optional

from samples.csv_parser.psyop_target_dto import PsyOpTargetDTO
from data.parse_url.url_parser import UrlParser


class TargetMapper:
    """"""
    DEFAULT_DATETIME: str = "1970-01-01 00:00 +0300"
    DEFAULT_BOOLEAN: bool = False
    DEFAULT_INTEGER: int = -1

    @staticmethod
    def csv_to_domain(row: list[str]) -> PsyOpTargetDTO:
        """"""
        __number: int = TargetMapper.get_int_or_default(row[0])
        username: str = row[1]
        subscribers: int = TargetMapper.get_int_or_default(row[2])
        link: str = row[3]
        seized_top: bool = TargetMapper.get_bool_or_default(row[4])
        views: int = TargetMapper.get_int_or_default(row[5])
        likes: int = TargetMapper.get_int_or_default(row[6])
        shares: int = TargetMapper.get_int_or_default(row[7])
        comments: int = TargetMapper.get_int_or_default(row[8])
        published_at: str = TargetMapper.DEFAULT_DATETIME
        reason: str = row[10]
        status: str = " ".join(row[11].upper().split("_"))
        through_suggestion: bool = TargetMapper.get_bool_or_default(row[12])
        platform: str = UrlParser.get_platform(link)
        content_id: str = UrlParser.get_content_id(link)
        title: str = f""

        return PsyOpTargetDTO(
            _number=__number,
            username=username,
            title=title,
            subscribers=subscribers,
            link=link,
            platform=platform,
            content_id=content_id,
            seized_top=seized_top,
            views=views,
            likes=likes,
            shares=shares,
            comments=comments,
            published_at=published_at,
            reason=reason,
            status=status,
            through_suggestion=through_suggestion
        )

    @staticmethod
    def get_int_or_default(value: str) -> Optional[int]:
        return int(value) if str(value).isdigit() else TargetMapper.DEFAULT_INTEGER

    @staticmethod
    def get_bool_or_default(value: str) -> bool:
        if value == "FALSE":
            return False
        elif value == "TRUE":
            return True
        else:
            return TargetMapper.DEFAULT_BOOLEAN
