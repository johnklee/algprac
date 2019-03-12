#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/array-left-rotation/problem
'''
import math
import os
import random
import re
import sys


def sl(n, a, d):
    na = []
    for i in xrange(n):
        na.append(str(a[(i + d) % n]))

    return ' '.join(na)

tary = [1, 2, 3, 4, 5]
d = 5
print("{}".format(sl(len(tary), tary, d)))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        pass
