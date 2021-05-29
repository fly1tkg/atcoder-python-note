## TLE
# n = int(input())

# def fib(i):
#   if i == 0 or i == 1:
#     return 1
  
#   return fib(i-1) + fib(i-2)

# print(fib(n))

n = int(input())

if n == 0 or n == 1:
  print(1)
  exit()

a = 1
b = 1
tmp = 0

for _ in range(n - 1):
  tmp = a
  a += b
  b = tmp

print(a)
