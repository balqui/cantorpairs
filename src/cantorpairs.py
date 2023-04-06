'''
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528, april 2023 onwards 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

First steps towards a Partial Recursive Functions lab.

Pair / unpair functions adapted from https://en.wikipedia.org/wiki/Pairing_function
'''

from functools import cache

def isqrt(n):
    "int square root via binary search"
    def rr(n, k):
        """
        Pre: k <= sqrt(n)
        Post: a <= sqrt(n) < b and b - a = k
        """
        if 4*k*k > n:
            return k, 2*k
        a, b = rr(n, 2*k)
        m = (a + b)//2 # m = a + k
        if m*m <= n:
            return m, b
        else:
            return a, m
    assert n >= 0
    if n == 0:
        return 0
    return rr(n, 1)[0]

@cache
def _unpair(z):
    '''
    math.sqrt fails with big numbers, e.g. the
    decoding of dp(10, 10^17) comes out wrong
    '''
    assert z > 0
    w = (isqrt(8*(z - 1) + 1) - 1)//2
    t = (w*w + w)//2
    x = z - 1 - t
    return x, w - x

@cache
def dp(x, y):
    return ((x + y)*(x + y + 1))//2 + x + 1

def pr_l(z):
    if z == 0:
        return 0
    return _unpair(z)[0]

def pr_r(z):
    if z == 0:
        return 0
    return _unpair(z)[1]

def tup_e(*nums):
    '''
    nums: arbitrary quantity of numbers to encode the sequence;
    fall back into the iterable version, the tuple cast will do nothing
    '''
    return tup_i(nums)

def tup_i(nums):
    '''
    nums expected to be an iterable here;
    the reversed nature of the encoding needs to 
    expand it into a sequence;
    end of sequence (= empty sequence) encoded 
    by 0 in its role of # nil, out of dotted pair range
    '''
    t = 0 
    for i in reversed(tuple(nums)):
        t = dp(i, t)
    return t

@cache
def s_tup(t, k):
    '''
    suffix tuple: t assumed a tuple of at least k components,
    return the suffix tuple from k-th on;
    t itself for k == 0, empty tuple 0 if k larger than len of t
    '''
    if t == 0:
        "empty tuple or original k too large"
        return 0
    if k == 0:
        "full suffix"
        return t
    return s_tup(pr_r(t), k-1)

def pr(t, k):
    '''
    projection function: get the k-th component;
    returns nonsense (probably a zero) if k too large
    '''
    return pr_l(s_tup(t, k))
