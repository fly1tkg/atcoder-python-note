A, B = map(int, input().split())

res = (B / 100) * A

if res.is_integer():
  res = int(res)

print(res)
