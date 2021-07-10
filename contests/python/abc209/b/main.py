def resolve():
  N, X = map(int, input().split())
  A = list(map(int, input().split()))

  price = sum(A) - (len(A) // 2)

  if X >= price:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
  resolve()