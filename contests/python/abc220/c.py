N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)

lap = X // sumA
restX = X - (sumA * lap)

# print(sumA, lap, restX)

count = 0

for a in A:
  restX -= a
  count += 1
  if restX < 0:
    break

print(count+(lap*len(A)))