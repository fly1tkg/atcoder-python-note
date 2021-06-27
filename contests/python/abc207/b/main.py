a, b, c, d = map(int, input().split())

blue = a
red = 0

if b >= c * d:
  print(-1)
  exit()

ans = 0

while blue > red * d:
  blue += b
  red += c
  ans += 1

print(ans)

