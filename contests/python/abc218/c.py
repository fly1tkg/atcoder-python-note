N = int(input())

S = []
T = []

for _ in range(N):
  S.append(list(input()))

for _ in range(N):
  T.append(list(input()))

sp = []

for i in range(N):
  for j in range(N):
    if S[i][j] == '.': continue
    sp.append((i, j,))

tp = []

for i in range(N):
  for j in range(N):
    if T[i][j] == '.': continue
    tp.append((i, j,))

print(sp)
print(tp)

def trans(l, o):
  trans_list = []

  for i in l:
    trans_list.append((i[0]-o[0], i[1]-o[1]))
  
  return set(trans_list)

sps = trans(sp, sp[0])
print('sps', sps)

for o in tp:
  tp1 = trans(tp, o)

  if tp1 == sps:
    print('Yes')
    exit()
  
  tp2 = set()
  for i in tp1:
    tp2.add((i[1], -i[0]))

  if tp2 == sps:
    print('Yes')
    exit()

  tp3 = set()
  for i in tp1:
    tp3.add((-i[1], -i[0]))

  if tp3 == sps:
    print('Yes')
    exit()

  tp4 = set()
  for i in tp1:
    tp4.add((i[0], -i[1]))
  
  if tp4 == sps:
    print('Yes')
    exit()

  print(tp1)
  print(tp2)
  print(tp3)
  print(tp4)
