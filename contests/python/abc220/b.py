K = int(input())
A, B = input().split()

a1 = 0
b1 = 0

for idx, a in enumerate(reversed(list(A))):
  # print(idx, a)
  # print((K**idx) * int(a))
  a1 += (K**idx) * int(a)

for idx, b in enumerate(reversed(list(B))):
  b1 += (K**idx) * int(b)

# print(a1, b1)
print(a1 * b1)