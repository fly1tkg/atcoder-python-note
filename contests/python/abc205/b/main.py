N = int(input())
A = map(int, input().split())

res = [False] * N

for a in A:
  res[a-1] = True

# print(res)

if sum(res) == N:
  print('Yes')
else:
  print('No')
