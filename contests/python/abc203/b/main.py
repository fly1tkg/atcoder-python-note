N, K = map(int, input().split())

result = 0

for n in range(N):
  result += (100 * (n+1) * K) + sum(range(1, K+1))

print(result)
