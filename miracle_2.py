#!/usr/bin/env python3

# "The Miracle Sudoku 2" by Ri Sa
# https://www.youtube.com/watch?v=LwkNChSO2yE

from utils import init, solve, knight
from itertools import product

s, board = init()

# knight moves
for r, c in product(range(9), repeat=2):
  for nr, nc in knight(r, c):
    s.add(board[r][c] != board[nr][nc])

# thermometers
thermometers = (
  ((1, 4), (0, 3), (1, 2), (2, 3)),
  ((2, 4), (1, 3)),
  ((1, 6), (2, 5), (3, 4)),
  ((2, 6), (3, 7), (4, 6), (3, 5)),
  ((5, 6), (6, 7), (7, 6), (6, 5), (5, 4)),
  ((6, 6), (7, 5), (6, 4), (5, 5)),
)
for t in thermometers:
  for i, (r, c) in enumerate(t[:-1]):
    nr, nc = t[i+1]
    s.add(board[r][c] < board[nr][nc])

# given
s.add(board[1][3] == 9)

# solve
solve(s, board)
