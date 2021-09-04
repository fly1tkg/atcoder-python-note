X, Y = input().split('.')

Y = int(Y)

if Y <= 2:
  print(f'{X}-')
elif Y <= 6:
  print(X)
else:
  print(f'{X}+')
