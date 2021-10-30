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
    d1 = math.degrees(math.atan2(dx1, dy1))
    if d1 < 0:
      d1 += 180

    for n in range(m+1, N):
      dx2 = (P[l][0] - P[n][0])
      dy2 = (P[l][1] - P[n][1])
      d2 = math.degrees(math.atan2(dx2, dy2))
      if d2 < 0:
        d2 += 180

      print(d1, d2)
      if not math.isclose(d1, d2, rel_tol=0.001):
        print(True)
        ans += 1
      
print(ans)
