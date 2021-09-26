Q = int(input())

A = []

query_list = []

for _ in range(Q):
  query_list.append(input())

for query in query_list:
  x = query[0]

  if x == '1':
    A.append(int(query.split()[1]))
  elif x == '2':
    print(A.pop(0))
  else:
    A.sort()

