import sys
sys.setrecursionlimit(10 ** 9)

N, M, K = map(int, input().split())

def calc(n, m, k):
  if n == 0:
    return 0
  
  if m == 0:
    return m ** k
  
  return calc(n-1, m, k) + calc(n, m-1, k)

print(calc(N, M, K))