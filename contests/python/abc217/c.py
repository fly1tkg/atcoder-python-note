N = int(input())

P = list(map(int, input().split()))
Q = [0] * N

for i in range(1, N+1):
  Q[P[i-1]-1] = i

print(*Q)
