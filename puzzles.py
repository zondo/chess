"""Chess puzzles in FEN format.
"""

import yaml
from pathlib import Path
from fenwrite import write_svg


def get_puzzles(path="puzzles.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def dump_puzzle(name, fen, dirname=None):
    dirname = Path(dirname or ".")
    dirname.mkdir(exist_ok=True)

    prefix = dirname / name
    write_svg(fen, prefix.with_suffix(".svg"))
    print(f"Wrote {name}")


def dump(dirname=None):
    categories = get_puzzles()
    for category, puzzles in categories.items():
        for name, fen in sorted(puzzles.items()):
            dump_puzzle(name, fen, dirname)
