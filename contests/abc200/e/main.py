import math

n, k = map(int, input().split())

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

sum = 0
x = 3

while(True):
    tmp = sum
    tmp += comb(x, 3)
    if tmp >= k:
        break
    sum = tmp
    x += 1

print(sum)
print(x)

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
