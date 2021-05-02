H, W = map(int, input().split())

map = []

for i in range(H):
    map.append([1 if s == '#' else 0 for s in input()])
    
# print(map)

def d(h, w):
    if h < 0 or w < 0:
        return 0

    try:
        return map[h][w]
    except:
        return 0

for h in range(H):
    results = []

    for w in range(W):

        if map[h][w] == 1:
            results.append('#')
            continue

        result = d(h-1,w-1) + d(h-1,w) + d(h-1,w+1)
        result += d(h,w-1) + d(h,w+1)
        result += d(h+1,w-1) + d(h+1,w) + d(h+1,w+1)

        results.append(str(result))
    
    print(''.join(results))
