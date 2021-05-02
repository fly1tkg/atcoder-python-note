n = int(input())
 
l = []
for i in range(0, n):
    l.append(int(input()))
 
l.sort(reverse=True)
 
result = 1
current = l[0]
 
for j in range(0, n):
    if j == 0:
        continue
 
    if current > l[j]:
        result += 1
        current = l[j]
 
print(result)