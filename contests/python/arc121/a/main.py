n = int(input())

h = []

xmax = 0
xmin = 0
ymax = 0
ymin = 0

for _ in range(n):
  x, y = map(int, input().split())
  xmax = max(xmax, x)
  xmin = min(xmin, x)
  ymax = max(ymax, y)
  ymin = min(ymin, y)
  h.append([x, y])

xmid = (xmax + xmin) // 2
ymid = (ymax + ymin) // 2

q1 = []
q2 = []
q3 = []
q4 = []

qs = [q1, q2, q3, q4]

for i in range(n):
  x, y = h[i]

  if x >= xmid and y >= ymid:
    q1.append([x,y])
  elif x < xmid and y >= ymid:
    q2.append([x,y])  
  elif x < xmid and y < ymid:
    q3.append([x,y])  
  elif x >= xmid and y < ymid:
    q4.append([x,y])

top = 0
second = 0

tophouse = []
secondhouse = []

for n in range(4):
  for m in range(n, 4):
    for i in qs[n]:
      for j in qs[m]:
        result = max(abs(i[0] - j[0]), abs(i[1] - j[1]))

        if result >= top:
          second = top
          top = result
          secondhouse = tophouse
          tophouse = [i, j]
        elif result >= second:
          second = result
          secondhouse = [i, j]

print(tophouse)
print(top)
print(secondhouse)

print(second)