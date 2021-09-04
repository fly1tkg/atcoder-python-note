import heapq

N = int(input())
A = []
heapq.heapify(A)

inf = 10 ** 9 + 10

for i, x in enumerate(map(int, input().split())):
  heapq.heappush(A, (inf - x, i+1,))

heapq.heappop(A)
ans = heapq.heappop(A)

print(ans[1])
