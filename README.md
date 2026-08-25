# cantorpairs
## (Almost) Cantor pairing and extension to tupling

Ancillary project for the related initiative PReFScript
(<https://github.com/balqui/prefscript>).
Implements (a slight variant of) the Cantor pairing function 
and its projections. See the example at the end of this file
for a quick review.

Project started: mid Germinal 2003.
Current version: 1.0, early Fructidor 2026.

Not pip-installable as of today. Handled as a Git submodule
of the `prefscript` repo. If you need to use it standalone,
feel free to download the source or clone the repo and then
put it where your `python` can see it. 
File `src/cantorpairs/cantorpairs_src.py` probably suffices.

Follows relatively closely <https://en.wikipedia.org/wiki/Pairing_function>
with a slight difference: Pairs will work like dotted pairs 
in creating tuples, hence a `nil` notion is necessary 
(cf. <https://en.wikipedia.org/wiki/Cons>).
To this end, the natural number zero is used as `nil` and the 
dotted pair is a bijection between `N x N` and `N - {0}`. 
The formulas have been adapted slightly to obtain this bijection.

Functions are defined in file `cantorpairs_src.py` whereas file 
`cp_ex.py` contains the examples given below. The `__init__` file
in the upper folder allows one to import functions from outside.
Compare `cp_ex.py` and `cp_ex_alt.py` to see how to import the 
exposed functions in each case. This repo contains also right now
an `Ensure` class left undocumented _on purpose_.

### Pairing examples

(Dotted) Pair formation (a.k.a. `cons` to Lispers) is `dp(x, y)`. 
The inverses are the left and right projections `pr_L` (for **L**eft)
and `pr_R` (for **R**ight), extended to map to zero for input zero. 
Thus, `dp(pr_L(x), pr_R(x)) == x` if `x != 0`.

Early versions of these sources used `pr_l` (an ell, for **l**eft)
which was easily confused with number 1. Currently both projections
are marked with upper case `L` and (accordingly) `R`.

According to <https://import-as.github.io/>, it is infrequent that
packages are imported `as cp`; the ones that do are `cvxpy`, `copy`,
`cupy` and `chaospy`: there is no consensus and most of these packages 
are unlikely to be used in the same project as `cantorpairs`. Hence, 
the user project `prefscript` runs a command `import cantorpairs as cp`
and I suggest to maintain that shorthand when possible, while importing 
as `cpt` (for "Cantor pairs and tuples") only in case of conflict.

```
import cantorpairs as cp

for i in range(4):
  for j in range(4):
    print(i, j, cp.dp(i, j))

for i in range(90, 100):
  print(cp.pr_L(i), cp.pr_R(i), cp.dp(cp.pr_L(i), cp.pr_R(i)), i) 
```

### Tupling exemples

In order to have unbounded-length tuples, a tuple is either empty 
(mapped to zero as "nil") or a pair formed by the first element and 
the rest of the tuple. All this is very traditional in some cultures.

There are two functions that form tuples: in one, `tup_e`, 
the arguments are **e**xplicitly integers, an arbitrary number 
of them. In the other, `tup_i`, the single argument is an 
**i**terable of integers. We can extract values from tuples 
(besides using `pr_L` and `pr_R`) with the suffix tuple function 
`s_tup(t, k)` that discards the first `k` components and returns 
the tuple starting at position `k` (counting from zero) and the 
general projection function `pr(t, k)` that retrieves the component 
at position `k` (again counting from zero).

Conversely, `seq(z)` iterates enough so as to unpack the sequence
encoded by `z` and return it in the form of a Python list.

```
t = cp.tup_e(4, 7, 56, 101)
for i in range(5):
    'last call is actually out of range'
    print(cp.pr(t, i))

st = cp.s_tup(t, 2)
print(st)
for i in range(3):
    print(cp.pr(st, i))

print(cp.seq(54321)

print(t, cp.seq(t))

while t:
    print(t, cp.pr_L(t))
    t = cp.pr_R(t)

t = cp.tup_i(range(8, 16))
while t:
    print(t, cp.pr_L(t))
    t = cp.pr_R(t)

```
