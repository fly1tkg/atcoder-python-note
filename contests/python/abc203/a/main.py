a,b,c = map(int, input().split())

result = 0

if a == b:
  result = c
elif a == c:
  result = b
elif b == c:
  result = a

print(result)
