import re

S = input()

if re.match('.*er$', S):
  print('er')
elif re.match('.*ist$', S):
  print('ist')
