from collections import deque

N, K = map(int, input().split())

C = list(map(int, input().split()))

d = deque()
for i in range(K):
  d.append(C[i])

ans = 0

for i in range(0, N-K+1):
  d.pop()
  d.append(C[i+K-1])
  # print(d)
  ans = max(ans, len(set(d)))

print(ans)

