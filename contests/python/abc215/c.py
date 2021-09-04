import itertools

S, K = input().split()

K = int(K)

l = list(set(map(lambda x: ''.join(x), itertools.permutations(list(S)))))

l.sort()

print(l[K-1])
