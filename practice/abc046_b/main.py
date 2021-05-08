# 問題: https://atcoder.jp/contests/abc046/tasks/abc046_b
# 解説: https://img.atcoder.jp/data/arc/062/editorial.pdf

n, k = map(int, input().split())

# k * (k-1)^(n-1)
result = k * pow(k-1, n-1)

print(result)