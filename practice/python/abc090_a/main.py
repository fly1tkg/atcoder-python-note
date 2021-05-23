# 問題: https://atcoder.jp/contests/abc087/tasks/arc090_a

n = int(input())

# print(n)

a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))

# print(a)

max = 0

for x in range(n): # 下にいくとき
    result = 0
    for j in range(n):
        if j < x:
            result += a[0][j]
        if j == x:
            result += a[0][j]
            result += a[1][j]
        if j > x:
            result += a[1][j]
        
        if max < result:
            max = result

print(max)
