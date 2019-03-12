#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/the-great-xor/problem
'''
import math
import os
import random
import re
import sys


def n2b(n, l=None):
    bits = map(int, list("{0:0b}".format(n)))

    if l and len(bits) < l:
        for i in range(l-len(bits)):
            bits.insert(0, 0)

    return bits


def b2n(bits):
    val = 0
    d = 0
    for i in bits[::-1]:
        val += i * math.pow(2, d)
        d += 1

    return int(val)


def bnot(bits):
    nbits = []
    for i in bits:
        if i:
            nbits.append(0)
        else:
            nbits.append(1)

    return nbits


cnpn_cache = {}
def cnpn(c, n):
    if c == n:
        return 1
    elif n == 1:
        return c
    elif (c, n) in cnpn_cache:
        return cnpn_cache[(c, n)]
    else:
        c_n = cnpn(c-1, n-1) + cnpn(c-1, n)
        cnpn_cache[(c, n)] = c_n
        return c_n

# Complete the theGreatXor function below.
def theGreatXor(x):
    if x <= 1:
        return 0
    elif x == 2:
        return 1
    else:
        cnt = 0
        bits = n2b(x)
        #print("{}:{}".format(x, bits))
        for i in xrange(len(bits)):
            if bits[i] == 0:
                cnt += math.pow(2, len(bits)-1-i)

        return int(cnt)
        


print("{}".format(theGreatXor(10)))
print("{}".format(theGreatXor(2)))
