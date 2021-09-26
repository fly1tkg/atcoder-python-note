X = input()
N = int(input())
S = [input() for _ in range(N)]

D = dict()

for idx, x in enumerate(list(X)):
  D[x] = chr(ord("a") + idx)

ans = []

for s in S:
  i = []
  for c in list(s):
    i.append(D[c])
  
  ans.append((''.join(i), s,))

ans.sort(key=lambda tup: tup[0])

for a in ans:
  print(a[1])
