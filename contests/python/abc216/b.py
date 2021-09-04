N = int(input())

names = set()

for _ in range(N):
  S, T = input().split()
  names.add(f'{S} {T}')

if len(names) == N:
  print('No')
else:
  print('Yes')
