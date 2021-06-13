N = int(input())

A = list(map(int, input().split()))

sum = 0

for a in A:
  if a > 10:
    sum += (a - 10)

print(sum)