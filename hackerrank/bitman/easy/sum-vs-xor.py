#!/usr/bin/env python
import math
import os
import random
import re
import sys

def xor(abits, bbits):
    bits = []
    for i in range(len(abits)):
        if abits[i] != bbits[i]:
            bits.append(1)
        else:
            bits.append(0)

    return bits


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


# Complete the solve function below.
def solve_n(n):
    if n <= 1:
        return 1

    nbits = n2b(n)
    nval = b2n(bnot(nbits))
    print('n={}; nn={}'.format(n, nval))
    cnt = 2
    #print("nbits={}".format(nbits))
    for i in xrange(1, nval):
        obits = n2b(i, len(nbits))
        xbits = xor(n2b(i, len(nbits)), nbits)
        #print("obits={}\nxbots={}".format(obits, xbits))
        #print("{} + {} = {}".format(i, n , i+n))
        xor_val = b2n(xbits)
        #print("{} xor {} = {}".format(i, n, xor_val))
        if i + n == b2n(xor(n2b(i, len(nbits)), nbits)):
            #print('Got {}...'.format(i))
            cnt += 1
        #print("")

    return cnt


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

def solve(n):
    if n <= 1:
        return 1

    cnt = 1
    nbits = n2b(n)
    zcnt = len(filter(lambda e: e==0, nbits))
    for i in range(1, zcnt+1):
        cnt += cnpn(zcnt, i)

    return cnt


#print("{}".format(solve(1000000000000000))) 
print("{}".format(solve(10)))
#print("{}".format(solve(5)))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    (5, 2), 
                    (10, 4), 
                    (0, 1), 
                    (1, 1), 
                    (1000000000000000, 1073741824)
                 ]

        for n, a in tdatas:
            r = solve(n)
            self.assertEqual(a, r, "Expect={}; Real={}".format(a, r)) 
