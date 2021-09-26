from itertools import combinations

N = int(input())

P = {}

for _ in range(N):
  x, y = list(map(int, input().split()))
  if not y in P:
    P[y] = set()

  P[y].add(x)

PL = []
for k, v in P.items():
  PL.append(v)

# print(PL)

L = len(PL)

ans = 0

for i in range(L-1):
  for j in range(i+1, L):
    # print(i, j)
    ans += (len(list(combinations((PL[i] & PL[j]), 2))))

print(ans)
