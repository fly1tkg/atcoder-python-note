import math

a, b, k = map(int, input().split())

result = ''

def count(a, b):
    # print(a, b)
    return int(math.factorial(a + b) / (math.factorial(a) * math.factorial(b)))

# print(next(a,b))

total = 0

while True:
    # print("result: {}, a: {}, b: {}".format(result, a, b))
    if a == 0 and b == 0:
        print(result)
        exit()

    if a == 0:
        total += count(a, b - 1)
        result = result + 'b'
        b -= 1
        continue
    elif b == 0:
        result = result + 'a'
        a -= 1  
        continue
    
    c = count(a - 1, b)
    d = count(a, b - 1)
    # print('right:', c)
    # print('left:', d)
    # print('total:', c + total)

    if a > 0 and k <= (c + total):
        result = result + 'a'
        a -= 1
    else:
        total += c
        result = result + 'b'
        b -= 1
