#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
'''
import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    bc = 0
    for i in range(i, j + 1):
        ri = int(str(i)[::-1])
        #print("i={}; ri={}".format(i, ri))
        if abs(ri - i) % k == 0:
            bc += 1

    return bc


#print("{}".format(beautifulDays(20, 23, 6)))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [ (20, 23, 6, 2)]
        for i, j, k, a in tdatas:
            r = beautifulDays(i, j, k)
            self.assertEqual(a, r, 'Expr={}; Real={}'.format(a, r))
