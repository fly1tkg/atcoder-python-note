import itertools

N = []

for s in list(input()):
  N.append(int(s))

A = []

ans = 0

def ltoi(l):
  if l[0] == 0:
    return 0

  l2 = []

  for i in l:
    l2.append(str(i))
    
  
  return int(''.join(l2))

for t in range(1, (len(N) // 2) + 1):
  for p in list(itertools.permutations(range(len(N)), t)):
    A = []
    B = []

    for i in range(len(N)):
      if i in p:
        A.append(N[i])
      else:
        B.append(N[i])
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    ans = max(ans, ltoi(A) * ltoi(B))

print(ans)
