s = set(['ABC', 'ARC', 'AGC', 'AHC'])

for _ in range(3):
  s.remove(input())

print(list(s)[0])
