"""Solve mate-in-2 chess puzzles.
"""

import chess


def solve_puzzle(fen):
    for move, replies in mate_in_2(fen):
        print(f"1. {move}")
        for reply, mating_move in sorted(replies.items()):
            print(f"1. ... {reply:6} 2. {mating_move}")


def mate_in_2(fen):
    board = chess.Board(fen)

    # Look at all first moves for white.
    for move in legal_moves(board):
        # Keep track of Black's replies, and White's and mating moves.
        replies = {}

        # Does Black have a move that avoids mate?
        avoidmate = False

        # Check Black's replies.
        for reply in legal_moves(board):
            # Is there a mating move from this position?
            canmate = False
            for mating_move in legal_moves(board):
                if board.is_checkmate():
                    replies[reply] = mating_move
                    canmate = True
                    break

            # If not, Black can escape.
            if not canmate:
                avoidmate = True
                break

        # If black can't escape mate, it's a solution.
        if not avoidmate:
            yield move, replies


def legal_moves(board):
    for move in board.legal_moves:
        try:
            san = board.san(move)
            board.push(move)
            yield san
        finally:
            board.pop()
