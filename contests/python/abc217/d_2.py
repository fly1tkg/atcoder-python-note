import bisect

L, Q = map(int, input().split())

query_list = []
prints = []
cuts = []
for i in range(Q):
  c, x = map(int, input().split())
  if c == 2:
    prints.append(i)
  else:
    cuts.append((i, x,))

cuts.sort(key=lambda tup: tup[1])

cut_timing = []
cut_position = []

for cut in cuts:
  cut_timing.append(cut[0])
  cut_position.append(cut[1])

for p in prints:
