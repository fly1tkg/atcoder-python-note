S = input()
chokudai = {
  'c':[],
  'h':[],
  'o':[],
  'k':[],
  'u':[],
  'd':[],
  'a':[],
  'i':[],
}
pow10_9 = 10 ** 9 + 7

for i, s in enumerate(list(S)):
  if s in chokudai.keys():
    chokudai[s].append(i)

ans = 0
for c in chokudai['c']:
  for h in chokudai['h']:
    if c > h:
      continue
    for o in chokudai['o']:
      if h > o:
        continue
      for k in chokudai['k']:
        if o > k:
          continue
        for u in chokudai['u']:
          if k > u:
            continue
          for d in chokudai['d']:
            if u > d:
              continue
            for a in chokudai['a']:
              if d > a:
                continue
              for i in chokudai['i']:
                if a > i:
                  continue
                # print(c, h, o, k, u, d, a, i)
                ans += 1
                ans = ans % pow10_9
print(ans)
