import math
import collections

n = int(input())
a = list(map(int, input().split()))

b = list(map(lambda x: x % 200, a))
commons = collections.Counter(b).most_common()
# print(commons)

ans = 0

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for x, y in commons:
    if y < 2:
        break
    
    ans += comb(y, 2)

print(ans)
