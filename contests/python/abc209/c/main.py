
pow10_7 = 10 ** 9 + 7

def resolve():  
  N = int(input())
  C = list(map(int, input().split()))
  C.sort()

  res = C[0]
  C = C[1:]

  for i, c in enumerate(C):
    res *= (c - (i + 1)) % pow10_7

  if res <= 0:
    print(0)
  else:
    print(res % pow10_7)
  
if __name__ == "__main__":
  resolve()