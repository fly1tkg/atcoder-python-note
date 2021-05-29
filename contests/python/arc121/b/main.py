import bisect

N = int(input())

r = []
g = []
b = []

for _ in range(2 * N):
  a, c = map(str, input().split())

  if c == 'R':
    r.append(int(a))
  elif c == 'G':
    g.append(int(a))
  else:
    b.append(int(a))

target = []

for l in [r, g, b]:
  if len(l) % 2 != 0:
    l.sort()
    target.append(l)

if len(target) == 0:
  print(0)
  exit()

result = float('inf')
blen = len(target[1])

# print(target[1])

for a in target[0]:
  # print('a:',a)
  i = bisect.bisect_left(target[1], a)
  # print('i:', i)
  # print('b:', target[1][i])
  # print(abs(a - target[1][i]))

  if i >= blen:
    result = min(result, abs(a - target[1][i]))
  else:
    # print('c:', target[1][i-1])
    result = min(result, abs(a - target[1][i]), abs(a - target[1][i+1]))

print(result)
