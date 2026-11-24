"""Standalone implementation: 22 N Queens."""
from collections import deque
from heapq import heappush, heappop
from math import inf

def n_queens(n):
    solutions, cols, diag1, diag2 = [], set(), set(), set()
    board = [-1] * n
    def backtrack(row):
        if row == n:
            solutions.append([
                "".join("Q" if board[r] == c else "." for c in range(n))
                for r in range(n)
            ])
            return
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            board[row] = col
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            backtrack(row + 1)
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
    backtrack(0)
    return solutions

if __name__ == "__main__":
    print("Number of solutions:", len(n_queens(4)))
