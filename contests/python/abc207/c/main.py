N = int(input())

l = []

for _ in range(N):
  l.append(list(map(int, input().split())))

def solve(item1, item2):
  t1, l1, r1 = item1
  t2, l2, r2 = item2

  if l1 < r2:
    if l2 < r1:
      # print(1, item1, item2)
      return 1
    
    if l2 == r1 and (t1 == 1 or t1 == 3) and (t2 == 1 or t2 == 2):
      # print(2, item1, item2)
      return 1
  else:
    if l1 < r2:
      # print(3, item1, item2)
      return 1
    
    if l1 == r2 and (t2 == 1 or t2 == 3) and (t1 == 1 or t1 == 2):
      # print(4, item1, item2)
      return 1

  return 0

ans = 0

for i in range(N):
  for j in range(i+1, N):
    ans += solve(l[i], l[j])

print(ans)
