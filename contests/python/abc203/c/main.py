N, K = map(int, input().split())

if K == 0:
  print(0)
  exit()

friends = []

for _ in range(N):
  n, m = map(int, input().split())
  friends.append((n, m,))

friends.sort(key=lambda tup: tup[0])

# print(friends)

pos = 0

for (n, m,) in friends:
  # print('n, m:', n, m)

  cost = n - pos
  # print('cost:', cost)

  # tadorituku
  if K >= cost:
    K += m - cost
    pos += cost
  else: # つかない
    break


pos += K
print(pos)
