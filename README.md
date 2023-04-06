# cantorpairs
## (Almost) Cantor pairing and extension to tupling

Ancillary project for a forthcoming initiative. Implements (a slight variant of) the Cantor pairing function and its projections.

Not pip-installable as of today. Download the source. File src/cantorpairs.py suffices.

Following relatively closely <https://en.wikipedia.org/wiki/Pairing_function>

Differences: Pairs will work like dotted pairs in creating tuples, so a "nil" is necessary (cf. <https://en.wikipedia.org/wiki/Cons>).
To this end, the natural number zero is used as "nil" and the dotted pair is a bijection between `NxN` and `N-{0}`. The formulas
have been adapted slightly to obtain this bijection.

Functions are defined in file cantorpairs.py whereas file cpt_ex.py contains the examples given below.

### Pairing examples

(Dotted) Pair formation (a.k.a. `cons` to Lispers) is `dp(x, y)`. The inverses are the left and right projections `pr_l` 
(an ell, not 1, number one) and `pr_r`, extended to map to zero for input zero. Thus `dp(pr_l(x), pr_r(x)) == x` if `x != 0`.

For the time being, I import as `cpt` for "cantor pairs and tuples".

```
import cantorpairs as cpt

for i in range(4):
  for j in range(4):
    print(i, j, cpt.dp(i, j))

for i in range(90, 100):
  print(cpt.pr_l(i), cpt.pr_r(i), cpt.dp(cpt.pr_l(i), cpt.pr_r(i)), i) 
```

### Tupling exemples

In order to have unbounded-length tuples, a tuple is either empty (mapped to zero as "nil") or a pair formed by the first element and the rest of the tuple. All this is very traditional in some cultures.

There are two functions that form tuples: in one, `tup_e`, the arguments are **e**xplicitly integers, an arbitrary number of them. 
In the other, `tup_i`, the single argument is an **i**terable of integers. We can extract values from tuples (besides using `pr_l` 
and `pr_r`) with the suffix tuple function `s_tup(t, k)` that discards the first `k` components and returns the tuple starting at 
position `k` (counting from zero) and the general projection function `pr(t, k)` that retrieves the component at position `k`
(again counting from zero).

```
t = cpt.tup_e(4, 7, 56, 101)
for i in range(5):
    'last call is actually out of range'
    print(cpt.pr(t, i))

st = cpt.s_tup(t, 2)
print(st)
for i in range(3):
    print(cpt.pr(st, i))

while t:
    print(t, cpt.pr1(t))
    t = cpt.pr2(t)

t = cpt.tup_i(range(8, 16))
while t:
    print(t, cpt.pr1(t))
    t = cpt.pr2(t)
```

