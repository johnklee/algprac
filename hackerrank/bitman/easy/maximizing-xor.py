#!/usr/bin/env python
import math
import os
import random
import re
import sys

def bit2int(bits):
    sum = 0
    for i in range(len(bits)):
        sum += math.pow(2, i) * bits[-(i+1)]

    return int(sum)

def int2bit(val, flen=None):
    bits = map(int, list('{0:0b}'.format(val)))
    if flen:
        if len(bits) < flen:
            for i in range(flen - len(bits)):
                bits.insert(0, 0)

    return bits

def notBits(bits):
    nbits = []
    for b in bits:
        if b == 1:
            nbits.append(0)
        else:
            nbits.append(1)

    return nbits


def xorBits(abits, bbits):
    nbits = []
    for i in range(len(abits)):
        if abits[i] + bbits[i] == 1:
            nbits.append(1)
        else:
            nbits.append(0)

    return nbits

# Complete the maximizingXor function below.
def maximizingXor(l, r):    
    rbits = int2bit(r)
    #print('rbits: {}\t{}'.format(rbits, bit2int(rbits)))

    max_xor_val = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            jbits = int2bit(j)
            ibits = int2bit(i, len(jbits))
            xor_val = bit2int(xorBits(ibits, jbits))
            if xor_val > max_xor_val:
                max_xor_val = xor_val

    #lbits = int2bit(l, len(rbits))
    #nbits = notBits(rbits)
    #xbits = xorBits(rbits, nbits)

    #print('rbits: {}\t{}'.format(rbits, bit2int(rbits)))
    #print('lbits: {}\t{}'.format(lbits, bit2int(lbits)))
    #print('nbits: {}\t{}'.format(nbits, bit2int(nbits)))
    #print('xbits: {}\t{}'.format(xbits, bit2int(xbits)))

    return max_xor_val


print("{}".format(maximizingXor(1, 10)))
print("{}".format(maximizingXor(10, 15)))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    (1, 10, 15),
                    (10, 15, 7)
                 ]

        for l, r, a in tdatas:
            v = maximizingXor(l, r)
            self.assertEqual(a, v, 'Expect={}; Real={}'.format(a, v))
