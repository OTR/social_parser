""""""
import csv
from pathlib import Path
import json

from samples.csv_parser.target_mapper import TargetMapper
from samples.csv_parser.psyop_target_dto import PsyOpTargetDTO
from samples.csv_parser.highlighter_dto import HighlighterDTO


class CsvLoader:
    """"""
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    INPUT_TARGETS_FILE = PROJECT_ROOT / ".data" / "psyop_targets.csv"
    INPUT_HIGHLIGHTERS_FILE = PROJECT_ROOT / ".data" / "highlighters.csv"
    OUTPUT_TARGETS_FILE = PROJECT_ROOT / "app" / "fixtures" / "targets.json"
    OUTPUT_HIGHLIGHTERS_FILE = PROJECT_ROOT / "app" / "fixtures" / "highlighters.json"

    @staticmethod
    def parse_targets_csv() -> list:
        """"""
        targets = []

        with open(CsvLoader.INPUT_TARGETS_FILE, 'r') as file1:
            reader = csv.reader(file1)
            header = next(reader)
            for row in reader:
                if row[3] and row[3].startswith("https"):
                    try:
                        target: PsyOpTargetDTO = TargetMapper.csv_to_domain(row)
                        targets.append(target)
                    except ValueError as e:
                        if e.args[0] == "Unknown platform t":
                            pass
                        else:
                            raise e

        return targets

    @staticmethod
    def parse_highlighters_csv() -> list:
        highlighters = []

        with open(CsvLoader.INPUT_HIGHLIGHTERS_FILE, "r") as file1:
            reader = csv.reader(file1)
            header = next(reader)
            for row in reader:
                hightlighter = HighlighterDTO(
                    channel_id=row[0],
                    channel_title=row[1],
                    reason=row[2]
                )
                highlighters.append(hightlighter)

        return highlighters

    @staticmethod
    def create_targets_json(targets: list[PsyOpTargetDTO]) -> None:
        """"""
        targets: list[PsyOpTargetDTO] = CsvLoader.parse_targets_csv()
        json_to_dump = list()
        for i, target in enumerate(targets, start=1):
            json_to_dump.append(
                {
                    "model": "app.ContentModel",
                    "pk": i,
                    "fields": target.get_fields_as_dict()
                }
            )
        with open(CsvLoader.OUTPUT_TARGETS_FILE, "w") as file1:
            json.dump(fp=file1, obj=json_to_dump)

    @staticmethod
    def create_highlighters_json():
        """"""
        highlighters: list[HighlighterDTO] = CsvLoader.parse_highlighters_csv()
        json_to_dump = list()
        for i, highlighter in enumerate(highlighters, start=1):
            json_to_dump.append({
                "model": "app.HighlightModel",
                "pk": i,
                "fields": highlighter.get_fields_as_dict()

            })
        with open(CsvLoader.OUTPUT_HIGHLIGHTERS_FILE, "w") as file1:
            json.dump(fp=file1, obj=json_to_dump)


if __name__ == "__main__":
    CsvLoader.create_highlighters_json()
