#!/usr/bin/env python3

# "Chinese Coin" by Aspartagcus
# https://www.youtube.com/watch?v=TELB3fZDG2E

from utils import init, solve
from itertools import tee
from more_itertools import grouper

s, board = init()

# coin
coin = (
  (5, 3), (5, 4), (6, 4), (6, 5), (5, 6), (4, 6), (3, 6), (2, 6), (2, 5),
  (2, 4), (2, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 3), (7, 3),
  (8, 3), (8, 2), (7, 1), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 1),
  (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 7), (2, 8), (3, 8), (4, 8),
  (5, 8), (6, 8), (7, 7), (8, 6), (8, 5), (8, 4)
)
a, b = tee(grouper(2, coin))
next(b, None)
for ((x1r, x1c), (x2r, x2c)), ((y1r, y1c), (y2r, y2c)) in zip(a, b):
  s.add(10*board[x1r][x1c] + board[x2r][x2c] < 10*board[y1r][y1c] + board[y2r][y2c])

# solve
solve(s, board)
