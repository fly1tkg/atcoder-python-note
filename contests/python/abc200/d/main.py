import itertools

n = int(input())
a = list(map(int, input().split()))

lst = [list(i) for i in itertools.product(['b', 'c', 'none'], repeat=n)]
# print(lst)

for l in lst:
    bsum = 0
    blist = []
    csum = 0
    clist = []
    for i in range(n):
        if l[i] == 'b':
            blist.append(i)
            bsum += a(i)
        elif l[i] == 'c':
            clist.append(i)
            csum += a(i)

    if b % 200 == c % 200:
        print("YES")
        print("{} {}", lent(b))
        print("{} {}", )


# print("NO")

# perlist = list(itertools.permutations(range(n), n))

# for t in perlist:
#     print("{}{}{}".format(t[0], t[1], t[2]))

# kind = ['b', 'c', 'none']

# kindlist = []
# for i in range(n):
#     l = []
#     for k in kind:
#         l.append(kind)


# bsum = 0
# blist = []
# csum = 0
# clist = []
# for i in range(n):
#     for k in kind:
#         if kind == 'b':
#             blist.append(i)
#             b += a(i)
#         elif kind == 'c':
#             clist.append(i)
#             c += a(i)

# if b % 200 == c % 200:
#     print("YES")
#     print("{} {}", lent(b))
#     print("{} {}", )


# print("NO")