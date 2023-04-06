'''
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528, april 2023 onwards 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

First steps towards a Partial Recursive Functions lab.

Examples of usage of pairing and tupling.
'''

import cantorpairs as cpt

for i in range(4):
  for j in range(4):
    print(i, j, cpt.dp(i, j))

for i in range(90, 100):
  print(cpt.pr_l(i), cpt.pr_r(i), cpt.dp(cpt.pr_l(i), cpt.pr_r(i)), i) 

t = cpt.tup_e(4, 7, 56, 101)
for i in range(5):
    'last call is actually out of range'
    print(cpt.pr(t, i))

st = cpt.s_tup(t, 2)
print(st)
for i in range(3):
    print(cpt.pr(st, i))

while t:
    print(t, cpt.pr_l(t))
    t = cpt.pr_r(t)

t = cpt.tup_i(range(8, 16))
while t:
    print(t, cpt.pr_l(t))
    t = cpt.pr_r(t)


