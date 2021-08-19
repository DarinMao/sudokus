from z3 import Distinct, If, Int, Solver, sat
from itertools import product
from more_itertools import grouper

valid = lambda r, c: r >= 0 and r < 9 and c >= 0 and c < 9
z3abs = lambda x: If(x >= 0, x, -x)

def init():
  s = Solver()
  b = [[Int(f'r{r}c{c}') for c in range(9)] for r in range(9)]

  # all numbers 1-9
  for r, c in product(range(9), repeat=2):
    s.add(b[r][c] >= 1)
    s.add(b[r][c] <= 9)

  # rows are distinct
  for r in range(9):
    s.add(Distinct(b[r]))

  # cols are distinct
  for c in range(9):
    s.add(Distinct([b[r][c] for r in range(9)]))

  # boxes are distinct
  for sr, sc in product(range(3), repeat=2):
    s.add(Distinct([b[sr*3+r][sc*3+c] for r, c in product(range(3), repeat=2)]))

  return s, b

def display(board, model):
  s = ''
  divider = ('+'+'-'*(2*3+1))*3 + '+\n'
  s += divider
  for bigrow in grouper(3, board):
    for row in bigrow:
      s += '| '
      for chunk in grouper(3, row):
        s += ' '.join(str(model[x]) for x in chunk)
        s += ' | '
      s += '\n'
    s += divider
  return s

def solve(s, board):
  assert s.check() == sat
  m = s.model()
  print(display(board, m))

def knight(r, c):
  for s1, s2 in product((-1, 1), repeat=2):
    d1, d2 = 1*s1, 2*s2
    nr, nc = r+d1, c+d2
    if valid(nr, nc):
      yield nr, nc
    nr, nc = r+d2, c+d1
    if valid(nr, nc):
      yield nr, nc

def king(r, c):
  for dr, dc in product((-1, 0, 1), repeat=2):
    if dr == 0 and dc == 0: continue
    nr, nc = r+dr, c+dc
    if valid(nr, nc):
      yield nr, nc

def ortho(r, c):
  for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    nr, nc = r+dr, c+dc
    if valid(nr, nc):
      yield nr, nc
