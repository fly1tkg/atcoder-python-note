H, W, C = map(int, input().split())

A = []

for _ in range(H):
  A.append(list(map(int, input().split())))

# print(A)
ans = float('inf')

for i1 in range(H):
  for j1 in range(W):
    for i2 in range(i1, H):
      for j2 in range(W):
        if i1 == i2 and j1 >= j2:
          continue

        c =  C * (abs(i1 - i2) + abs(j1 - j2))
        a =  A[i1][j1] + A[i2][j2] + c
        # print(i1, j1, i2, j2, A[i1][j1], A[i2][j2], c, a)
        ans = min(ans, a)

print(ans)