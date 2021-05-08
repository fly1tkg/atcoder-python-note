# 問題: https://atcoder.jp/contests/abc055/tasks/abc055_b
# 解説: https://img.atcoder.jp/arc069/editorial.pdf
n = int(input())

result = 1

for i in range(1, n + 1):
    result = result * i % 1000000007

print(result)