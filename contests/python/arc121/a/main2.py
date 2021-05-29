n = int(input())

harfn = n // 2

h = []
xlist = []
ylist = []

for i in range(n):
  x, y = map(int, input().split())
  h.append([x, y])
  xlist.append((i, x,))
  ylist.append((i, y,))

sortedx = sorted(xlist, key=lambda it: it[1])
sortedy = sorted(ylist, key=lambda it: it[1])
# print(sortedx)
# print(sortedy)

xmin = sortedx[0]
xmax = sortedx[-1]
ymin = sortedy[0]
ymax = sortedy[-1]

sset = set([xmin[0], xmax[0], ymin[0], ymax[0]])

top = 0
second = 0

tophouse = set([-1, -1])
secondhouse = set([-1, -1])

# print(h)

for s in sset:
  for i in range(n):
    if i == s:
      continue

    currentset = set([s, i]) 

    if currentset == tophouse or currentset == secondhouse:
      continue
    
    # print(h[s], h[i])

    result = max(abs(h[s][0] - h[i][0]), abs(h[s][1] - h[i][1]))

    if result >= top:
      second = top
      top = result  
      secondhouse = tophouse
      tophouse = currentset
    elif result >= second:
      second = result
      secondhouse = currentset

# print(tophouse)
# print(top)
# print(secondhouse)
print(second)
