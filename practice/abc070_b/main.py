A, B, C, D = map(int, input().split())

result = 0

if A <= C:
    if B <= C:
        print(0)
    elif B <= D:
        print(B - C)
    else:
        print(D - C)
else:
    if D <= A:
        print(0)
    elif D <= B:
        print(D - A)
    else:
        print(B - A)