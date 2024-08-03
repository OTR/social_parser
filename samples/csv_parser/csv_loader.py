""""""
import csv
from pathlib import Path
import json

from samples.csv_parser.target_mapper import TargetMapper
from samples.csv_parser.psyop_target_dto import PsyOpTargetDTO


class CsvLoader:
    """"""
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    INPUT_FILE = PROJECT_ROOT / ".data" / "psyop_targets.csv"
    OUTPUT_FILE = PROJECT_ROOT / "app" / "fixtures" / "targets.json"

    @staticmethod
    def parse_csv() -> list:

        targets = []

        with open(CsvLoader.INPUT_FILE, 'r') as file:
            reader = csv.reader(file)
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
    def create_json(targets: list[PsyOpTargetDTO]) -> None:
        """"""


if __name__ == "__main__":
    targets: list[PsyOpTargetDTO] = CsvLoader.parse_csv()
    json_to_dump = list()
    for i, target in enumerate(targets, start=1):
        json_to_dump.append(
            {
                "model": "app.ContentModel",
                "pk": i,
                "fields": target.get_fields_as_dict()
            }
        )
    with open(CsvLoader.OUTPUT_FILE, "w") as file1:
        json.dump(fp=file1, obj=json_to_dump)
