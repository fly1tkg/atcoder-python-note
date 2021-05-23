s = list(input())
s.reverse()

result = []

for it in s:
    if it == '6':
        result.append('9')
    elif it == '9':
        result.append('6')
    else:
        result.append(it)

print(''.join(result))
