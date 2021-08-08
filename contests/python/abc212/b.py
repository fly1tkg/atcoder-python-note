x = [int(n) for n in list(input())]

if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
  print('Weak')
  exit()

cnt = 0

for i in range(3):
  n = x[i]
  
  if n == 9:
    n = 0
  else:
    n += 1
  
  if n == x[i+1]:
    cnt += 1

if cnt == 3:
  print('Weak')
else:
  print('Strong')
