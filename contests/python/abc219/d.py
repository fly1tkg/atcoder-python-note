N = int(input())
X, Y = map(int, input().split())

A = []
B = []
C = []

sumA = 0
sumB = 0

for _ in range(N):
  a, b = map(int,input().split())

  A.append(a)
  B.append(b)
  C.append(a+b)
  sumA += a
  sumB += b

if X > sumA or Y > sumB:
  print(-1)
  exit()

ans = 0

while X > 0 and Y > 0:
  if X > 0 and Y > 0:
    max_value = max(C)
    max_index = C.index(max_value)
    X -= A[max_index]
    Y -= B[max_index]

    A.pop(max_index)
    B.pop(max_index)
  elif Y <= 0:
    max_value = max(A)
    max_index = A.index(max_value)
    X -= max_value
    Y -= B[max_index]

    A.pop(max_index)
    B.pop(max_index)
  else:
    max_value = max(B)
    max_index = B.index(max_value)
    X -= A[max_index]
    Y -= max_value

    A.pop(max_index)
    B.pop(max_index)
  
  ans += 1

print(ans)
