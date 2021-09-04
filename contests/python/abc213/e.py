H, W = map(int, input().split())

S = []

for i in range(H):
  S.append(list(input()))

inf = 1000000

dp = []

dp.append([0] * (W + 2))

for _ in range(H+1):
  dp.append([0] * (W + 2))


for i in range(1, H+1):
  for j in range(1, W+1):
    if dp[i][j] != 0:
      continue
    
    if S[i-1][j-1] == '#':
      dp[i][j] = dp[i][j-1] + dp[i-1][j] + 1
      dp[i][j+1] = dp[i][j]
      dp[i+1][j] = dp[i][j]
      dp[i+1][j+1] = dp[i][j]
    else:
      dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp)

print(dp[H][W])
