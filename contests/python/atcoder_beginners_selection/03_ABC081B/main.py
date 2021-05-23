def half(arr):
    res = []
 
    for i in arr:
        i = i / 2
 
        if not i.is_integer():
            return (False, [])
 
        res.append(i)
    
    return (True, res)
 
length = int(input())
arr = map(int, input().split())
 
result = 0
 
while(True):
    (ok, arr) = half(arr)
    if ok:
        result += 1
    else:
        break
 
print(result)