A, B, C = map(int, input().split())

if C == 0:
  print('=')
  exit()

plus = C > 0

if C % 2 == 0:
  abs_a = abs(A)
  abs_b = abs(B)

  if abs_a > abs_b:
    print('>') if plus else print('<')
  elif abs_a < abs_b:
    print('<') if plus else print('>')
  else:
    print('=')
else:
  if A > B:
    print('>') if plus else print('<')
  elif A < B:
    print('<') if plus else print('>')
  else: # A == B
    print('=')
