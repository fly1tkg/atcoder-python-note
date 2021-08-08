import heapq

Q = int(input())

b = []
heapq.heapify(b)

a = 0

for i in range(Q):
  q = input()

  if q == '3':
    print(heapq.heappop(b) + a)
  
  else:
    m, x = map(int, q.split())

    if m == 1:
      heapq.heappush(b, x-a)

    if m == 2:
      a += x
