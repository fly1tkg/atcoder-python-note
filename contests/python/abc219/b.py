S = ['', input(), input(), input()]
T = map(int, list(input()))

ans = []

for t in T:
  ans.append(S[t])

print(''.join(ans))
