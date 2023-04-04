#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initializes an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    outcome = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                outcome.append([r, c])
                break
    return (outcome)
