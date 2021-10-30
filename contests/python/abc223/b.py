S = list(input())

lens = len(S)

def shift():
  s = S.pop(0)
  S.append(s)

ans = []

for _ in range(lens):
  ans.append(''.join(S))
  shift()

ans.sort()

print(ans[0])
print(ans[-1])
