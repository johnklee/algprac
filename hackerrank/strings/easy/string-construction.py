#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/string-construction/problem
'''

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    c = 0
    p = set()
    for i in s:
        if i in p:
            continue
        else:
            p.add(i)
            c += 1

    return c


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [('abcd', 4), ('abab', 2)]

        for s, a in tdatas:
            r = stringConstruction(s) 
            self.assertEqual(a, r, 'Exp={}; Rel={}'.format(a, r))
