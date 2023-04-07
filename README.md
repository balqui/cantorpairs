# cantorpairs
## (Almost) Cantor pairing and extension to tupling

Ancillary project for a forthcoming initiative. 
Implements (a slight variant of) the Cantor pairing function 
and its projections.

Not pip-installable as of today. Download the source. File src/cantorpairs.py suffices.

Following relatively closely <https://en.wikipedia.org/wiki/Pairing_function>

Differences: Pairs will work like dotted pairs in creating tuples, 
so a "nil" is necessary (cf. <https://en.wikipedia.org/wiki/Cons>).
To this end, the natural number zero is used as "nil" and the 
dotted pair is a bijection between `NxN` and `N-{0}`. The formulas
have been adapted slightly to obtain this bijection.

Functions are defined in file cantorpairs.py whereas file cp_ex.py 
contains the examples given below.

### Pairing examples

(Dotted) Pair formation (a.k.a. `cons` to Lispers) is `dp(x, y)`. 
The inverses are the left and right projections `pr_l` (an ell, 
not number 1) and `pr_r`, extended to map to zero for input zero. 
Thus `dp(pr_l(x), pr_r(x)) == x` if `x != 0`.

According to <https://import-as.github.io/>, it is infrequent that
packages are imported `as cp`; the ones that do are `cvxpy`, `copy`,
`cupy` and `chaospy`: there is no consensus and most of these 
packages are unlikely to be used in the same project as `cantorpairs`.
Hence I `import cantorpairs as cp` and suggest importing as `cpt`
(for "Cantor pairs and tuples") in case of conflict.

```
import cantorpairs as cp

for i in range(4):
  for j in range(4):
    print(i, j, cp.dp(i, j))

for i in range(90, 100):
  print(cp.pr_l(i), cp.pr_r(i), cp.dp(cp.pr_l(i), cp.pr_r(i)), i) 
```

### Tupling exemples

In order to have unbounded-length tuples, a tuple is either empty 
(mapped to zero as "nil") or a pair formed by the first element and 
the rest of the tuple. All this is very traditional in some cultures.

There are two functions that form tuples: in one, `tup_e`, 
the arguments are **e**xplicitly integers, an arbitrary number 
of them. In the other, `tup_i`, the single argument is an 
**i**terable of integers. We can extract values from tuples 
(besides using `pr_l` and `pr_r`) with the suffix tuple function 
`s_tup(t, k)` that discards the first `k` components and returns 
the tuple starting at position `k` (counting from zero) and the 
general projection function `pr(t, k)` that retrieves the component 
at position `k` (again counting from zero).

```
t = cp.tup_e(4, 7, 56, 101)
for i in range(5):
    'last call is actually out of range'
    print(cp.pr(t, i))

st = cp.s_tup(t, 2)
print(st)
for i in range(3):
    print(cp.pr(st, i))

while t:
    print(t, cp.pr1(t))
    t = cp.pr2(t)

t = cp.tup_i(range(8, 16))
while t:
    print(t, cp.pr1(t))
    t = cp.pr2(t)
```

