# 問題: https://atcoder.jp/contests/abc079/tasks/abc079_c
a, b, c, d = map(int, list(input()))

# print("{} {} {} {}".format(a,b,c,d))

oplist = ['+', '-']

def op(x, y, op):
    # print("{}{}{}".format(x, op, y))
    if op == '+':
        return x + y
    
    if op == '-':
        return x - y

for op1 in oplist:
    for op2 in oplist:
        for op3 in oplist:
            ans = 0
            ans = op(a, b, op1)
            ans = op(ans, c, op2)
            ans = op(ans, d, op3)

            if ans == 7:
                print("{}{}{}{}{}{}{}=7".format(a, op1, b, op2, c, op3, d))
                exit()
