""""""
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

PATH = Path(__file__).parent.parent.parent / ".data" / "psyop_targets.csv"


@dataclass
class PsyOpTarget:
    number: int
    username: str
    subscribers: int
    link: str
    seized_top: bool
    views: int
    likes: int
    shares: int
    comments: str
    added_date: str
    reason: str
    status: str
    through_suggestion: bool


class Mapper:
    @staticmethod
    def csv_to_domain(row: list[str]) -> PsyOpTarget:
        """"""
        number: int = Mapper.get_int_or_none(row[0])
        username: str = row[1]
        subscribers: int = Mapper.get_int_or_none(row[2])
        link: str = row[3]
        seized_top: bool = Mapper.get_bool_or_none(row[4])
        views: int = Mapper.get_int_or_none(row[5])
        likes: int = Mapper.get_int_or_none(row[6])
        shares: int = Mapper.get_int_or_none(row[7])
        comments: str = row[8]
        added_date: str = row[9]
        reason: str = row[10]
        status: str = row[11]
        through_suggestion: bool = Mapper.get_bool_or_none(row[12])

        return PsyOpTarget(
                number=number,
                username=username,
                subscribers=subscribers,
                link=link,
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


def parse():

    targets = []

    with open(PATH, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[3] and row[3].startswith("https"):
                target: PsyOpTarget = Mapper.csv_to_domain(row)
                targets.append(target)

                print(target)


if __name__ == "__main__":
    parse()
