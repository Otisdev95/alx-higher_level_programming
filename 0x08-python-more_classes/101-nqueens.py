#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initializes an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)



