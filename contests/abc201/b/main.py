n = int(input())
l = []

for i in range(n):
    name, h = input().split()
    l.append({
        'name': name,
        'h': int(h)
    })

l.sort(key=lambda k: k['h'], reverse=True)

print(l[1]['name'])
