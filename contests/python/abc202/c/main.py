import collections

n = int(input())
#print(n)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

aa = collections.Counter(a)
bb = collections.Counter(b)
cc = collections.Counter(c)

# print(aa)
# print(bb)
# print(cc)

dd = {}
for k, v in cc.items():
    if not b[k - 1] in dd.keys():
        dd[b[k - 1]] = 0
    dd[b[k - 1]] += v

# print(dd)

result = 0

for i, iv in aa.items():
    if i in dd.keys():
        result += iv * dd[i]

print(result)
