N = int(input())
X, Y = map(int, input().split())

A = []
B = []

sumA = 0
sumB = 0

for _ in range(N):
  a, b = map(int,input().split())

  A.append(a)
  B.append(b)
  sumA += a
  sumB += b

if X > sumA or Y > sumB:
  print(-1)
  exit()

