import math

N = int(input())

P = []

for _ in range(N):
  P.append(list(map(int, input().split())))

ans = 0

for l in range(N-2):
  for m in range(l+1, N-1):
    dx1 = (P[l][0] - P[m][0])
    dy1 = (P[l][1] - P[m][1])
    d1 = 0
    if dx1 == 0:
      d1 = float('inf')
    elif dy1 != 0:
      d1 = dx1 / dy1

    for n in range(m+1, N):
      dx2 = (P[l][0] - P[n][0])
      dy2 = (P[l][1] - P[n][1])
      d2 = 0
      if dx2 == 0:
        d2 = float('inf')
      elif dy2 != 0:
        d2 = dx2 / dy2

      if math.isinf(d1) and math.isinf(d2):
        continue

      if math.isclose(d1, d2):
        continue

      ans += 1
      
print(ans)
