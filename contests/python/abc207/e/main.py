import math
def comb(n,r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

N = int(input())

A = list(map(int, input().split()))
lenA = len(A)

ans = 0

if A[N-1] % lenA == 0:
  ans += 1

for n in range(1, lenA + 1):
  for j in range(1, lenA + 1 - n):
    print(n, j)
    print(A[(lenA - n):])
    if sum(A[(lenA - n):]) % (j + 1) == 0:
      c = comb(lenA - n - 1, j - 1)
      print('comb:', c)
      ans += c % (10 ** 9 + 7)

print(int(ans))