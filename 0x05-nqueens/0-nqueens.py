#!/usr/bin/python3
"""
this program solves the n queens problem
"""

import sys


def nqueens(n):
    """Solve the N queens problem"""
    def can_place(pos, ocuppied_positions):
        """Checkif a queen can be placed in a position"""
        for i in range(ocuppied_positions):
            occupied = board[i] == pos
            occupied = occupied or board[i] - pos == ocuppied_positions - i
            occupied = occupied or board[i] - pos == i - ocuppied_positions
            if (occupied):
                return False
        return True

    def place_queen(n, ocuppied_positions, result):
        """Place a queen in a position and then call itself recursively"""
        if ocuppied_positions == n:
            result.append(board[:])
            return
        for i in range(n):
            if can_place(i, ocuppied_positions):
                board[ocuppied_positions] = i
                place_queen(n, ocuppied_positions + 1, result)

    result = []
    board = [-1] * n
    place_queen(n, 0, result)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = nqueens(n)
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])