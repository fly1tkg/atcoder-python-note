P = map(int, input().split())

res = []

for p in P:
  res.append(chr(96+p))

print(''.join(res))
