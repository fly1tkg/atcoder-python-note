import itertools
import collections


N = int(input())
S = list(input())

ans = N

ans += len(list(itertools.combinations(S, 2))) % 998244353
ans += len(list(itertools.combinations(S, 3))) % 998244353

for a in list(itertools.combinations(S, 3):
  if a[0] == a[1] and

print(ans)

count = collections.Counter(S)
print(count)

for c in count:
  if count[c] < 3:
    continue

  ans += (count[c] - 3) % 998244353
    
print(ans % 998244353)