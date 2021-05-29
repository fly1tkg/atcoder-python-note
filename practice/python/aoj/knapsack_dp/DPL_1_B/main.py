N, W = map(int, input().split())

weight = []
value = []

for i in range(N):
  y, x = map(int, input().split())
  weight.append(x)
  value.append(y)

dp = [[0]*(W+1) for j in range(N+1)]

for i in range(N):
  # print(weight[i], value[i])

  for w in range(W+1):
    if w >= weight[i]:
      if (w >= weight[i]):
        dp[i+1][w] = max(dp[i][w-weight[i]] + value[i], dp[i][w])
    else:
      dp[i+1][w] = dp[i][w]

print(dp[N][W])
