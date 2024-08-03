""""""
import csv
from pathlib import Path

from samples.csv_parser.target_mapper import TargetMapper
from samples.csv_parser.psyop_target_dto import PsyOpTargetDTO


PATH = Path(__file__).parent.parent.parent / ".data" / "psyop_targets.csv"


def parse_csv():

    targets = []

    with open(PATH, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[3] and row[3].startswith("https"):
                try:
                    target: PsyOpTargetDTO = TargetMapper.csv_to_domain(row)
                    targets.append(target)
                    print(target)
                except ValueError as e:
                    if e.args[0] == "Unknown platform t":
                        pass
                    else:
                        raise e


if __name__ == "__main__":
    parse_csv()
