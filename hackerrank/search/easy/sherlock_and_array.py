#!/usr/bin/env python
import sys

r'''
https://www.hackerrank.com/challenges/sherlock-and-array/problem
'''

def solve(a):
    # Complete this function
    return rsolve(a)

def rsolve(a):
    if len(a) == 1:
        return 'YES'
    elif len(a) == 2:
        return 'NO'
    elif len(a) == 3:
        return 'YES' if a[0] == a[2] else 'NO'
    else:
        return _rsolve(a, len(a)/2, 0, len(a) - 1)


def _rsolve(a, p, s, e):
    lsum = sum(a[:p])
    rsum = sum(a[p+1:])
    if lsum == rsum:
        return 'YES'
    elif lsum > rsum:
        # Move left
        e = p - 1
        if e < s:
            return 'NO'
        m = (e + s) / 2
        return _rsolve(a, m, s, e)
    else:
        # Move right
        s = p + 1
        if s > e:
            return 'NO'
        m = (s + e) / 2
        return _rsolve(a, m, s, e)

print(solve([1, 2, 3]))
print(solve([1, 2, 3, 3]))
