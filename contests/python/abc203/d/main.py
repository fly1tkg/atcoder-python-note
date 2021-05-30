N, K = map(int, input().split())

A = []

for _ in range(N):
  A.append(list(map(int, input().split())))

med = float('inf')

med_pos = (K ** 2 // 2)

print('med_pos:',med_pos)
wide = N - K + 1

for i in range(wide):
  for j in range(wide):
    sq = []
    print('i,j:',i,j)
    for y in range(j, j+K):
      # print('y:', y)
      # print(wide + i)
      # print(A[y][i:(K + i)])
      sq += A[y][i:(K + i)]
    
    sq.sort(reverse=True)
    print(sq)
    print(len(sq))

    # print(med)
    # print(sq[med_pos])
    med = min(med, sq[med_pos])

print(med)