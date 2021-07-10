def resolve():
  A, B = map(int, input().split())
  res = B - A + 1
  if res > 0:
    print(res)
  else:
    print(0)

if __name__ == "__main__":
  resolve()