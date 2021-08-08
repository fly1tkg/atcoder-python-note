import bisect

N, M = map(int, input().split())

A = list(set(map(int, input().split())))
B = list(set(map(int, input().split())))

# A.sort()
B.sort()

# print(A)
# print(B)

# amin = A[0]
# amax = A[-1]

# bmin = B[0]
# bmax = B[-1]

# if amax <= bmin:
#   print(abs(bmin-amax))
#   exit()
# elif bmax <= amin:
#   print(abs(amin-bmax))
#   exit()

ans = float('inf')
lenb = len(B)

for a in A:
  pos = bisect.bisect_left(B, a)
  # print(pos)
  if pos == 0:
    if lenb == 1:
      ans = min(ans, abs(a - B[pos]))
    else:
      ans = min(ans, abs(a - B[pos]), abs(a - B[pos+1]))
  elif pos == lenb:
    ans = min(ans, abs(a - B[pos-1]))
  elif pos == lenb -1:
    ans = min(ans, abs(a - B[pos-1]), abs(a - B[pos]))
  else:
    ans = min(ans, abs(a - B[pos-1]), abs(a - B[pos]), abs(a - B[pos+1]))

print(ans)


# aleft = bisect.bisect_left(A, bmin)
# aright = bisect.bisect_right(A, bmax)
# print('a', aleft, aright)

# bleft= bisect.bisect_left(B, amin)
# bright = bisect.bisect_right(B, amax)
# print('b', bleft, bright)

# ans = float('inf')

# for i in range(aleft, aright):
#   for j in range(bleft, bright):
#     # print('ij', i, j)
#     ans = min(ans, abs(A[i] - B[j]))

# print(ans)
