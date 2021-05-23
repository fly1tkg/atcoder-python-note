# 問題: https://atcoder.jp/contests/abc060/tasks/abc060_b
# 解説: https://img.atcoder.jp/arc073/editorial.pdf

a,b,c = map(int, input().split())

# 7x = 2 mod 5

n = a % b

if n == c:
    print("YES")
    exit()

i = 2
while(True):
    result = (i * n) % b

    if n == result:
        print("NO")
        break
    
    if result == c:
        print("YES")
        break

    i += 1
