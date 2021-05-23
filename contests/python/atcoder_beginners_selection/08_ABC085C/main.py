n, y = map(int, input().split())
 
def search(n, y):
    for a in range(0, n + 1):
        for b in range(0, n - a + 1):
            c = n - a - b
            if (10000 * a + 5000 * b + 1000 * c) == y:
                print("{} {} {}".format(a,b,c))
                return True
 
if not search(n, y):
    print("-1 -1 -1")