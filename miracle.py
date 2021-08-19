#!/usr/bin/env python3

# "The Miracle" by Mitchell Lee
# https://www.youtube.com/watch?v=yKf9aUIxdb4

from utils import init, solve, king, knight, ortho, z3abs
from itertools import chain, product

s, board = init()

# chess moves
for r, c in product(range(9), repeat=2):
  for nr, nc in chain(knight(r, c), king(r, c)):
    s.add(board[r][c] != board[nr][nc])

# orthogonally adjacent
for r, c in product(range(9), repeat=2):
  for nr, nc in ortho(r, c):
    s.add(z3abs(board[r][c] - board[nr][nc]) > 1)

# given
s.add(board[4][2] == 1)
s.add(board[5][6] == 2)

# solve
solve(s, board)
