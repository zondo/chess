from puzzles import get_puzzles, dump_puzzle, dump
from solve import solve_puzzle

puzzles = get_puzzles()
fuddler = puzzles["fuddler"]

# dump("puzzles")

month = "2022-12"
fen = fuddler[month]
dump_puzzle(month, fen, dirname="puzzles")

print()
print(month)
solve_puzzle(fen)
