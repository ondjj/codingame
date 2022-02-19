H, M = map(int, input().split())

if (H - 1 < 0) and (M - 45 < 0):
  print(H + 23, (M+60)-45)
elif (H -1 > 0) and (M -45 > 0):
  print(H, M)

   
