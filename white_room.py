#!/usr/bin/env python3

# "White Room" by Philip Newman
# https://www.youtube.com/watch?v=ejhtYYvUs5M

from utils import init, solve
from z3 import Distinct

s, board = init()

# cages
cages = (
  (7, ((1, 1), (2, 1), (3, 1))),
  (5, ((1, 5), (1, 6))),
  (6, ((2, 6), (2, 7))),
  (6, ((3, 5), (3, 6))),
  (23, ((5, 2), (5, 3), (6, 3))),
  (15, ((5, 8), (6, 8))),
  (17, ((6, 2), (7, 2))),
  (3, ((8, 5), (8, 6))),
)
for total, cells in cages:
  cells = [board[r][c] for r, c in cells]
  s.add(Distinct(cells))
  s.add(sum(cells) == total)

# solve
solve(s, board)
