N = int(input())

D = []

for _ in range(N):
  A, B = map(int, input().split())
  D.append((A,B,))

X = [0]
Y = [0]

for idx, d in enumerate(D):
  X.append(X[idx] + (d[0] / d[1]))

# print(X)

for idx, d in enumerate(reversed(D)):
  Y.append(Y[idx] + (d[0] / d[1]))

# print(Y)

firex = 1
firey = 1

while True:
  x = X[firex]
  y = Y[firey]

  if x > y:
    firey += 1
  else:
    firex += 1
  
  if firex + firey == N:
    break

# print(firex, firey)

ans = 0

for i in range(firex):
  ans += D[i][0]

# print(ans)

if X[firex] <= Y[firey]:
  a = D[firex][0] - (D[firex][1] * (X[firex] - Y[firey-1]))
  ans += a / 2
else:
  a = D[firex-1][0] - (D[firex-1][1] * (Y[firey] - X[firex-1]))
  ans -= a / 2

print(ans)