H, W, N = map(int,input().split())

cards = []

uniqA = set()
uniqB = set()

for _ in range(N):
  A, B = map(int, input().split())
  uniqA.add(A)
  uniqB.add(B)
  cards.append((A, B,))

orderA = sorted(uniqA)
orderB = sorted(uniqB)

dictA = {}
dictB = {}

for i, a in enumerate(orderA):
  dictA[a] = i + 1

for i, b in enumerate(orderB):
  dictB[b] = i + 1

for c in cards:
  print(dictA[c[0]], dictB[c[1]])

