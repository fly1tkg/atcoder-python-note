import sys

m = 2 * (10 ** 5) + 10

sys.setrecursionlimit(m)
N = int(input())

roads = [[] for _ in range(m)]
visited = [False] * m

for i in range(N-1):
  A, B = map(int, input().split())
  roads[A].append(B)
  roads[B].append(A)

ans = []

def dfs(i):
  ans.append(str(i))
  visited[i] = True
  for j in sorted(roads[i]):
    if not visited[j]:
      dfs(j)
      ans.append(str(i))

dfs(1)

print(' '.join(ans))
