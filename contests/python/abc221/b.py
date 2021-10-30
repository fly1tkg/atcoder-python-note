S = input()
T = input()

if S == T:
  print('Yes')
  exit()

for i in range(len(S)-1):
  ls = list(S)
  ls[i], ls[i+1] = ls[i+1], ls[i]
  
  if ''.join(ls) == T:
    print('Yes')
    exit()

print('No')
