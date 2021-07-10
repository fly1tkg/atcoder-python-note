import sys
sys.setrecursionlimit(10**9)

N, Q = None, None
road = {}

memo = {}

def check_memo(c, d):
  if c < d:
    key = f'{c}_{d}'
  else:
    key = f'{d}_{c}'
  
  if key in memo.keys():
    return memo[key]
  
  return None

def add_memo(a, b, n):
  if a < b:
    memo[f'{a}_{b}'] = n
  else:
    memo[f'{b}_{a}'] = n

def solve(start, dest, ok, n):
  cache = check_memo(start, dest)
  if cache:
    return cache

  n += 1
  ok.add(start)

  if dest in road[start]:
    add_memo(start, dest, 1)
    return n
  
  results = []

  for mid in road[start]:
    if mid in ok:
      continue

    results.append(solve(mid, dest, ok, n))

  if len(results) == 0:
    add_memo(start, dest, float('inf'))
    return float('inf')
  
  m = min(results)
  add_memo(start, dest, m)
  return m

def resolve():
  N, Q = map(int, input().split())

  for _ in range(N - 1):
    a, b = map(int, input().split())
    
    if a in road.keys():
      road[a].add(b)
    else:
      road[a] = {b}

    if b in road.keys():
      road[b].add(a)
    else:
      road[b] = {a}
  
  for _ in range(Q):
    c, d = map(int, input().split())

    if solve(c, d, set(), 0) % 2 == 0:
      print('Town')
    else:
      print('Road')


if __name__ == "__main__":
  resolve()
  print(road)
  print(memo)