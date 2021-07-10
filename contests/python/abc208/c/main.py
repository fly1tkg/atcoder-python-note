N, K = map(int, input().split())

alist = list(map(int, input().split()))

base = K // N
rest = K - (base * N)

# print(base, rest)

last = -1

if rest > 0:
  last = sorted(alist)[rest-1]

for a in alist:
  if a <= last:
    print(base + 1)
  else:
    print(base)
