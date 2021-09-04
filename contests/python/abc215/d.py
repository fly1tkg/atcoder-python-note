N, M = map(int, input().split())

A = list(map(int, input().split()))

factors = set()

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

for a in A:
  for n in factorization(a):
    factors.add(n[0])

if 1 in factors:
  factors.remove(1)

ans = 0
anslist = []

for x in range(1, M+1):
  result = True
  for f in factors:
    if x % f == 0:
      result = False
      break

  if result:
    ans += 1
    anslist.append(x)

print(ans)
for a in anslist:
  print(a)
