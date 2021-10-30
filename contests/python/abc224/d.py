M = int(input())

G = [[] for _ in range(10)]

for _ in range(M):
  u, v = map(int, input().split())
  G[u].append(v)
  G[v].append(u)

P = list(map(int, input().split()))

print(G)

def dfs(pos, count, goal, visited):
  if pos == goal:
    return count
    
  visited[pos] = True
  # print(G[pos])
  for g in G[pos]:
    if not visited[g]:
      res = dfs(g, count + 1, goal, visited)
      if res >= 0:
        return res
  
  return -1

ans = 0

for idx, p in enumerate(P):
  a = dfs(p, 0, idx+1, [False for _ in range(10)])
  print(a)
  if a >= 0:
    ans += a
  else:
    print(-1)
    exit()

print(ans)