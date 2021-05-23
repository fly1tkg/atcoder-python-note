tc, xc, yc = 0, 0, 0
 
for i in range(int(input())):
    t, x, y = map(int, input().split())
 
    dt = t - tc
    dist = abs(x - xc) + abs(y - yc)
    
    if dist > dt or (dt % 2) != (dist % 2):
        print("No")
        exit()
    
    tc, xc, yc = t, x, y
print("Yes")