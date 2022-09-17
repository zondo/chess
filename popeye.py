"""Popeye interface.
"""

import chess


popeye_template = """
begin
origin %s
pieces %s
option noboard variation
stipulation #2
end
"""


def popeye_to_fen(pop):
    """Convert popeye position to FEN.
    """

    colour = None
    board = chess.Board(None)

    for token in pop.split():
        if token in ("white", "black"):
            colour = token
        else:
            piece = token[0]

            if piece == 's':
                piece = 'n'
            if colour == 'white':
                piece = piece.upper()

            pos = token[1:].upper()
            square = getattr(chess, pos)

            piece = chess.Piece.from_symbol(piece)
            board.set_piece_at(square, piece)

    return board.fen()


def fen_to_popeye(fen):
    """Convert FEN to popeye position.
    """

    board = chess.Board(fen)
    white = []
    black = []

    for sq in chess.SQUARES:
        p = board.piece_at(sq)
        if p is None:
            continue

        p = str(p)
        s = chess.SQUARE_NAMES[sq]

        if p.isupper():
            col = white
            p = p.lower()
        else:
            col = black

        if p == 'n':
            p = 's'

        col.append(p + s)

    strings = ["white"] + white + ["black"] + black
    return " ".join(strings)
