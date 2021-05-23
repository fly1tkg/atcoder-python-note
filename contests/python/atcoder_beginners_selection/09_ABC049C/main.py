import re
 
s = input()
 
m = re.match(r'^(dream|dreamer|erase|eraser)*$', s)
 
if m:
    print("YES")
else:
    print("NO")