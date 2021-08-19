#!/usr/bin/env python3

# "Non-consecutive Killer" by spxtr
# https://www.youtube.com/watch?v=wO1G7GkIrWE

from utils import init, solve, ortho, z3abs
from z3 import Distinct
from itertools import product

s, board = init()

# cages
cages = (
  ((0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (3, 0), (3, 1)),
  ((0, 3), (0, 4), (0, 5), (1, 3), (1, 5), (2, 3), (3, 3), (4, 3), (4, 4)),
  ((0, 6), (0, 7), (0, 8), (1, 6), (1, 8), (2, 5), (2, 6), (3, 6)),
  ((1, 2), (2, 2), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 2), (5, 3)),
  ((1, 4), (2, 4), (3, 4), (3, 5), (4, 5), (4, 6)),
  ((1, 7), (2, 7), (2, 8), (3, 8), (4, 8), (5, 8)),
  ((4, 7), (5, 7), (6, 7), (6, 8), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)),
  ((5, 4), (5, 6), (6, 4), (6, 5), (6, 6), (7, 4), (7, 6), (8, 3), (8, 4)),
  ((6, 0), (6, 1), (6, 2), (6, 3), (7, 0), (7, 2), (8, 0), (8, 2)),
)

for cage in cages:
  s.add(Distinct([board[r][c] for r, c in cage]))

# orthogonally adjacent
for r, c in product(range(9), repeat=2):
  for nr, nc in ortho(r, c):
    s.add(z3abs(board[r][c] - board[nr][nc]) > 1)

# given
s.add(board[6][3] == 2)

# solve
solve(s, board)
