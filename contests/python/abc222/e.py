N, M, K = map(int, input().split())

A = map(int, input().split())

P = {}

for n in range(N-1):
  u, v = map(int, input().split())
  
  if u in P.keys():
    P[u].append((v, n,))
  else:
    P[u] = [(v, n,)]
  
  if v in P.keys():
    P[v].append((u, n,))
  else:
    P[v] = [(u, n,)]

print(P)

