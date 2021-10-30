from collections import deque
import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = deque(map(int, input().split()))
  
cache = dict()

def dfs(arr):  
  if len(arr) > 1:
    cache_key = ''.join([str(it) for it in arr])
    if cache_key in cache:
      return cache[cache_key]
    else:
      f = arr.copy()
      f.appendleft((f.popleft() + f.popleft()) % 10)
      resf = dfs(f)

      g = arr.copy()
      g.appendleft((g.popleft() * g.popleft()) % 10)
      resg = dfs(g)

      res = []
      for i in range(10):
        res.append((resf[i] + resg[i]) % 998244353)
      
      cache[cache_key] = res
    
    return res
  else:
    res = [0 for _ in range(10)]
    res[arr[0]] = 1
    return res

res = dfs(A)

for r in res:
  print(r)
