from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = Path.joinpath(ROOT,"src", "items.csv")
CSVTEST = Path.joinpath(ROOT,"tests", "items_test.csv")
NOTFILE = Path.joinpath(ROOT,"src", "items1.csv")