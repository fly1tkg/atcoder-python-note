H, W = map(int, input().split())

A = []

for h in range(H):
  A.append(list(map(int, input().split())))

I = []

for i1 in range(H-1):
  for i2 in range(i1+1, H):
    I.append((i1, i2,))

J = []

for j1 in range(W-1):
  for j2 in range(j1+1, W):
    J.append((j1, j2,))

# print(I)
# print(J)

res = True

for i in I:
  for j in J:
    if A[i[0]][j[0]] + A[i[1]][j[1]] > A[i[1]][j[0]] + A[i[0]][j[1]]:
      res = False

if res:
  print('Yes')
else:
  print('No')
