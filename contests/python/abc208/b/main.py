import math

pow_10_7 = 10 ** 7

n = []

i = 1
while True:
  a = math.factorial(i)
  n.append(a)
  # print(i, a)
  if pow_10_7 < a:
    # print(i)
    break
  i += 1

n.sort(reverse=True)
# print(n)

P = int(input())

res = 0
for m in n:
  if P >= m:
    r = P // m
    res += r
    P = P - (m * r)
    # print(m, r, P)
    if P == 0:
      break

print(res)
