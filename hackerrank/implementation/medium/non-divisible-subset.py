#!/usr/bin/env python3
r'''
https://www.hackerrank.com/challenges/non-divisible-subset/problem
'''
import math
import os
import random
import re
import sys

def all_nd(nds, v, k):
    for i in nds:
        if (i + v) % k == 0:
            return False

    return True

def nonDivisibleSubset(k, S):
    d = {x:[] for x in range(k)}
    for i in range(len(S)):
        d[S[i]%k].append(S[i])

    count = 0
    if len(d[0]) > 0:
        count = 1

    rS = set([(x, k-x) for x in range(1, k//2+1)])
    for i, j in rS:
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1 

    return count

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset_v1(k, S):
    nds = []
    s_len = len(S)
    for i in range(s_len):
        v = S[i]
        if v in nds:
            continue

        cnds = [v]
        for j in range(0, s_len):
            sv = S[j]
            if sv == v:
                continue

            if all_nd(cnds, sv, k):
                cnds.append(sv)

        if len(cnds) > len(nds):
            nds = cnds

    return len(nds)

print("{}".format(nonDivisibleSubset(5, [770528134, 663501748, 384261537, 800309024, 103668401, 538539662, 385488901, 101262949, 557792122, 46058493])))

import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        S = [770528134, 663501748, 384261537, 800309024, 103668401, 538539662, 385488901, 101262949, 557792122, 46058493]
        k = 5
        exp = 6
        rel = nonDivisibleSubset(k, S)
        self.assertEquals(exp, rel)
