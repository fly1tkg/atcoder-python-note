A, B = map(int, input().split())

if A > B:
  print('No')
  exit()

if (A * 6) < B:
  print('No')
  exit()

print('Yes')
