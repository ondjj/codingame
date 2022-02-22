import sys

while 0 < A and B < 10:
  A, B = map(int, sys.stdin.readline().split())

  if A and B == 0:
    break

  print(A+B)