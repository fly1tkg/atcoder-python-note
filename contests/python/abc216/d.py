import itertools
import queue
import copy

N, M = map(int, input().split())

K = []

for _ in range(M):
  input()
  K.append(list(map(int, input().split())))

q = queue.deque()
q.append(K)

result = False

while len(q) > 0:
  if result:
    break

  k = q.popleft()
  for a, b in itertools.combinations(range(M), 2):
    if len(k[a]) != 0 and len(k[b]) != 0 and k[a][0] == k[b][0]:
      k = copy.deepcopy(k)
      k[a].pop(0)
      k[b].pop(0)
      
      res = True
      for x in range(M):
        if len(k[x]) != 0:
          res = False
          break
      if res:
        result = True
      
      q.append(k)


if result:
  print('Yes')
else:
  print('No')
