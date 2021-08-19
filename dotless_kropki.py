#!/usr/bin/env python3

# "Dotless Kropki Sudoku X" by Phistomefel
# https://www.youtube.com/watch?v=1QP7yviZYTU

from utils import init, solve, ortho, z3abs
from z3 import Distinct
from itertools import product

s, board = init()

# diagonals are distinct
s.add(Distinct([board[x][x] for x in range(9)]))
s.add(Distinct([board[x][8-x] for x in range(9)]))

# orthogonally adjacent
for r, c in product(range(9), repeat=2):
  for nr, nc in ortho(r, c):
    s.add(z3abs(board[r][c] - board[nr][nc]) > 1)
    s.add(board[r][c] != board[nr][nc]*2)
    s.add(board[nr][nc] != board[r][c]*2)

# given
s.add(board[3][1] == 1)
s.add(board[3][7] == 2)
s.add(board[4][4] == 4)

# solve
solve(s, board)
