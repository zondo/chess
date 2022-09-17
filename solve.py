"""Solve chess puzzles.
"""

import chess


def solve_puzzle(fen):
    board = chess.Board(fen)

    for move in board.legal_moves:
        m1 = board.san(move)
        plays = []
        board.push(move)
        escape = False

        for move in board.legal_moves:
            m2 = board.san(move)
            board.push(move)
            allmate = False

            for move in board.legal_moves:
                m3 = board.san(move)
                board.push(move)
                mate = board.is_checkmate()
                board.pop()

                if mate:
                    plays.append([m2, m3])
                    allmate = True
                    break

            board.pop()
            if not allmate:
                escape = True
                break

        if not escape:
            print(m1)
            for m2, m3 in sorted(plays):
                print('   ', m2, m3)

        board.pop()


def do_move(board):
    for move in board.legal_moves:
        board.push(move)
        yield board.copy()
        board.pop()
