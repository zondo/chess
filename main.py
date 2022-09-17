from fuddler import puzzles, dump_puzzle
from solve import solve_puzzle

month = "2022-08"
fen = puzzles[month]
dump_puzzle(month, fen)
print()
print(month)
solve_puzzle(fen)