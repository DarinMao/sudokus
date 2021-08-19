#!/usr/bin/env python3

# "Arches and Arrows" by SudokuExplorer"
# https://www.youtube.com/watch?v=yy5Lo6O99CE

from utils import init, solve, knight
from itertools import product

s, board = init()

# knight moves
for r, c in product(range(9), repeat=2):
  for nr, nc in knight(r, c):
    s.add(board[r][c] != board[nr][nc])

# arrows
arrows = (
  ((2, 1), (3, 0), (4, 0), (5, 0)),
  ((2, 4), (3, 5), (4, 5), (5, 5)),
  ((3, 7), (4, 7), (3, 8)),
  ((5, 2), (4, 3), (3, 3), (2, 3)),
  ((5, 3), (4, 2), (3, 2), (2, 2)),
  ((8, 5), (7, 4), (6, 3)),
)
for (cr, cc), *arrow in arrows:
  s.add(board[cr][cc] == sum(board[r][c] for r, c in arrow))

# solve
solve(s, board)
