#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/service-lane/problem
'''
import math
import os
import random
import re
import sys


def gmin(n, s, e):
    min_val = sys.maxsize
    for i in range(s, e+1):
        if n[i] < min_val:
            min_val = n[i]

    return min_val

# Complete the serviceLane function below.
def serviceLane(n, cases):
    result = []

    for i, j in cases:
        result.append(gmin(n, i, j))

    return tuple(result)



#tn = [2, 3, 1, 2, 3, 2, 3, 3]
#tc = [
#        (0, 3),
#        (4, 6),
#        (6, 7),
#        (3, 5),
#        (0, 7)
#     ]
#print("{}".format(serviceLane(tn, tc)))


import unittest

class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [([2, 3, 1, 2, 3, 2, 3, 3], [(0, 3), (4, 6), (6, 7), (3, 5), (0, 7)], (1, 2, 3, 2, 1))]

        for n, cases, a in tdatas:
            r = serviceLane(n, cases)
            self.assertEqual(a, r, "Expr={}; Real={}".format(a, r))
