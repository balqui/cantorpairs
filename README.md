# cantorpairs
## (Almost) Cantor pairing and extension to tupling

Ancillary project for a forthcoming initiative. Implements (a slight variant of) the Cantor pairing function and its projections.

Not pip-installable as of today. Download the source.

Following relatively closely <https://en.wikipedia.org/wiki/Pairing_function>

Differences: Pairs will work like dotted pairs in creating tuples, so a "nil" is necessary (cf. <https://en.wikipedia.org/wiki/Cons>).
To this end, the natural number zero is used as "nil" and the dotted pair is a bijection between `NxN` and `N-{0}`. The formulas
have been adapted slightly to obtain this bijection.

### Pairing examples

(Dotted) Pair formation (a.k.a. `cons` to Lispers) is `dp(x, y)`. The inverses are projections `pr1` and `pr2`, extended 
to map to zero for input zero. Thus `dp(pr1(x), pr2(x)) == x` if `x != 0`.

For the time being, I import as `cpt` for "cantor pairs and tuples".

```
import cantorpairs as cpt

for i in range(4):
  for j in range(4):
    print(i, j, cpt.dp(i, j))

for i in range(1, 100):
  print(cpt.pr1(i), cpt.pr2(i), cpt.dp(cpt.pr1(i), cpt.pr2(i)), i) 
```

### Tupling exemples

In order to have unbounded-length tuples, a tuple is either empty (mapped to zero as "nil") or a pair formed by the first element and the rest of the tuple. All this is very traditional in some cultures.

There are two functions that form tuples: in one, `tup_e`, the arguments are **e**xplicitly integers, an arbitrary number of them. 
In the other, `tup_i`, the single argument is a **i**terable of integers.

