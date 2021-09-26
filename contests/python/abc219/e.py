option = []

for _ in range(4):
  first = -1
  last = -1

  for idx, a in enumerate(map(int, input().split())):
    if a == 1:
      if first == -1:
        first = idx
      
      last = max(last, idx)
  if first >= 0 and last >= 0:
    option.append(first+1)
    option.append(4-last)
  else:
    option.append(10)

print(option)

ans = 1

for o in option:
  ans *= o

print(ans)

    
