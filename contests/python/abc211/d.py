import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# print(g)

from collections import deque

def bfs(u):
  queue = deque([u])
  d = [None] * n
  d[u] = 0
  cnt = [0] * n
  cnt[0] = 1

  while queue:
    v = queue.popleft()
    # print('pop', v)
    for vv in g[v]:
      if d[vv] is None:
        d[vv] = d[v] + 1
        queue.append(vv)
        cnt[vv] = cnt[v]
      elif d[vv] == d[v] + 1:
        cnt[vv] += cnt[v]
        cnt[vv] %= 10**9+7 

  # print(d)
  # print(cnt)   
  return cnt[n-1]

ans = bfs(0)

print(ans)
