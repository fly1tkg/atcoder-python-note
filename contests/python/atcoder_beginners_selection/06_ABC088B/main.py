x = input()
arr = list(map(int, input().split()))
arr.sort(reverse = True)
 
alice = 0
bob = 0
 
for i in range(0, len(arr)):
    if i % 2 == 0:
        alice += arr[i]
    else:
        bob += arr[i]
 
print(alice - bob)