A, B, C = map(int, input().split())

ans = 0
res = False

for i in range(1, 1000):
  ans = C * i
  if A <= ans and ans <= B:
    res = True
    break

if res:
  print(ans)
else:
  print(-1)

