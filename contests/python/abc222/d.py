N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

mod = 998244353

dp = [[0] * 3010 for _ in range(3010)]

for i in range(A[0], B[0]+1):
  dp[1][i] = 1

for n in range(1, N):
  c = A[n]
  s = 0

  for i in range(0, c+1):
    s += dp[n][i]
  dp[n+1][c] = s % mod

  for c in range(A[n]+1, B[n]+1):
    s += dp[n][c]
    dp[n+1][c] = s % mod

print(sum(dp[N]) % mod)
