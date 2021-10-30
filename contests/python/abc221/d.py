import collections

N = int(input())

res = {}

for _ in range(N):
  A, B = map(int, input().split())

  for b in range(B):
    key = A+b
    if key in res.keys():
      res[key] += 1
    else:
      res[key] = 1
  
# print(res)
c = collections.Counter(res.values())

# print(c)

ans = []
for n in range(1, N+1):
  if n in c.keys():
    ans.append(c[n])
  else:
    ans.append(0)

print(*ans)