import bisect
import array

L, Q = map(int, input().split())

a = array.array('i', [L])

for q in range(Q):
  c, x = map(int, input().split())
  # print('c, x', c, x)
  if c == 1:
    bisect.insort(a, x)
  else:
    if len(a) == 1:
      print(L)
    else:
      # print(a)
      pos = bisect.bisect_left(a, x)
      # print('pos', pos)
      if pos == 0:
        print(a[pos])
      else:
        print(a[pos] - a[pos-1])
