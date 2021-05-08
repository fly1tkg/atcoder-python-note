# 問題: https://atcoder.jp/contests/abc048/tasks/abc048_b
# 解説: https://img.atcoder.jp/arc064/editorial.pdf

a, b, x = map(int, input().split())

# a <= x*i <= b
# -(-a//x) <= x <= b // x

n = -(-a//x)
m = b // x

print(m - n + 1)