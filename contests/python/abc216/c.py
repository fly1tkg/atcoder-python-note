import copy
N = int(input())

dp = [[] for _ in range(120)]
dp2 = [[] for _ in range(120)]

dp[0] = ['A']
dp2[0] = [1]


def find():
  for i in range(1, 120):
    for j in range(len(dp[i-1])):
      v = dp2[i-1][j] + 1
      if N == v:
        return dp[i-1][j] + 'A'
      dp[i].append(dp[i-1][j] + 'A')
      dp2[i].append(v)

      v = dp2[i-1][j] * 2
      if N == v:
        return dp[i-1][j] + 'B'
      dp[i].append(dp[i-1][j] + 'B')
      dp2[i].append(v)

ans = find()

print(ans)
