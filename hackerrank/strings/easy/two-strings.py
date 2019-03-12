#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/two-strings/problem
'''

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings_v1(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 'NO'

    cset= set()
    for c in s1:
        cset.add(c)

    for c in s2:
        cset.add(c)

    return 'YES' if len(s1) + len(s2) != len(cset) else 'NO'


def twoStrings(s1, s2):
    if len(s1) >= len(s2):
        ls = s1
        ss = s2
    else:
        ls = s2
        ss = s1

    cset = set()
    for c in ls:
        cset.add(c)

    for c in ss:
        if c in cset:
            return 'YES'

    return 'NO'


import unittest



class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    ('hello', 'world', 'YES'),
                    ('hi', 'world', 'NO')
                 ]

        for s1, s2, a in tdatas:
            r = twoStrings(s1, s2)
            self.assertEqual(a, r, 'Exp={}; Real={}'.format(a, r))
