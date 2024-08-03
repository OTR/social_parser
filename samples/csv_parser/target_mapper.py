""""""
from typing import Optional

from samples.csv_parser.psyop_target_dto import PsyOpTargetDTO
from service.parse_url.url_parser import UrlParser


class TargetMapper:
    """"""

    @staticmethod
    def csv_to_domain(row: list[str]) -> PsyOpTargetDTO:
        """"""
        number: int = TargetMapper.get_int_or_none(row[0])
        username: str = row[1]
        subscribers: int = TargetMapper.get_int_or_none(row[2])
        link: str = row[3]
        seized_top: bool = TargetMapper.get_bool_or_none(row[4])
        views: int = TargetMapper.get_int_or_none(row[5])
        likes: int = TargetMapper.get_int_or_none(row[6])
        shares: int = TargetMapper.get_int_or_none(row[7])
        comments: str = row[8]
        added_date: str = row[9]
        reason: str = row[10]
        status: str = row[11]
        through_suggestion: bool = TargetMapper.get_bool_or_none(row[12])
        platform: str = UrlParser.get_platform(link)
        content_id: str = UrlParser.get_content_id(link)

        return PsyOpTargetDTO(
            number=number,
            username=username,
            subscribers=subscribers,
            link=link,
            platform=platform,
            content_id=content_id,
            seized_top=seized_top,
            views=views,
            likes=likes,
            shares=shares,
            comments=comments,
            added_date=added_date,
            reason=reason,
            status=status,
            through_suggestion=through_suggestion
        )

    @staticmethod
    def get_int_or_none(value: str) -> Optional[int]:
        return int(value) if str(value).isdigit() else None

    @staticmethod
    def get_bool_or_none(value: str) -> Optional[bool]:
        if value == "FALSE":
            return False
        elif value == "TRUE":
            return True
        else:
            return None

