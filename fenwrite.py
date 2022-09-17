"""Write FEN positions to file.
"""

import chess
from chess import svg
from popeye import fen_to_popeye, popeye_template


def write_svg(fen, path):
    """Write a FEN position to an SVG file.
    """

    board = chess.Board(fen)
    with open(path, "w") as fp:
        fp.write(svg.board(board))


def write_popeye(fen, path, title):
    pop = fen_to_popeye(fen)
    with open(path, "w") as fp:
        fp.write(popeye_template.lstrip() % (title, pop))
