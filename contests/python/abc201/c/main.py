import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

str = input()
s = [char for char in str]

# print(s)

exists = []
not_exists = []
unknown = []

for i in range(10):

    if s[i] == 'o':
        exists.append(i)
    elif s[i] == 'x':
        not_exists.append(i)
    else:
        unknown.append(i)

print("exists: {}".format(exists))
print("not_exists: {}".format(not_exists))
print("unknown: {}".format(unknown))

if len(exists) > 4:
    print(0)
    exit()
 

h = permutations_count(len(unknown) + len(exists) + len(exists) - 1, (4-len(exists)))
print(h)

nh = permutations_count(len(exists), (4-len(exists)))

print(24 * h - nh)