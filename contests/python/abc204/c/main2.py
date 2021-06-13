N, M = map(int, input().split())

size = 2001
t = [set() for _ in range(size)]

for _ in range(M):
  a, b = map(int, input().split())
  t[a].add(a)
  t[b].add(a)
  t[b] = t[b].union(t[a])

def ex(a, b, n):
  for el in t[b]:
    t[b] = t[b].union(t[a])
    if n != len(t[b]):
      ex(a, b, n)

for i in range(1, size):
  for el in t[i]:
    t[i] = t[i].union(t[el])
    if len(t[i]) == M - 1:
      

result = 0

for s in t:
  result += len(s)

print(result)