N, M = map(int, input().split())

A = []

for n in range(2 * N):
  A.append(list(input()))

def battle(a, b):
  if a == b:
    return (0, 0,)

  if a == 'G' and b == 'C':
    return (1, 0,)
  
  if a == 'C' and b == 'P':
    return (1, 0,)
  
  if a == 'P' and b == 'G':
    return (1, 0,)
  
  return (0, 1,)

J = [[n, 0] for n in range(2 * N)]
# print(J)

for m in range(M):
  for n in range(N):
    # print(J[2*n], J[2*n+1])
    # print(A[J[2*n][0]][m], A[J[2*n+1][0]][m])
    a, b = battle(A[J[2*n][0]][m], A[J[2*n+1][0]][m])
    J[2*n][1] += a
    J[2*n+1][1] += b
  
  J.sort(key=lambda a: (-a[1], a[0]))
  # print(J)

for j in J:
  print(j[0] + 1)
