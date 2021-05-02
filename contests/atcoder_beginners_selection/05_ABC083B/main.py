n, a, b = map(int, input().split())
def exec(i):
    result = 0
    keta = [int(c) for c in str(i)]
    ketasum = sum(keta)
    if ketasum >= a and ketasum <= b:
        result += i
    return result
 
arr = [i for i in range(0, n + 1)]
print(sum(map(exec, arr)))