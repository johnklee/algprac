#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/repeated-string/problem
'''
import math
import os
import random
import re
import sys



# Complete the repeatedString function below.
def repeatedString(s, n):
    s_a = 0
    r_a = 0
    s_len = len(s)
    r_len = n % s_len
    for i in xrange(s_len):
        if s[i] == 'a':
            s_a += 1
            if i < r_len:
                r_a += 1

    print('s_len={}; r_len={}'.format(s_len, r_len))
    print('s_a = {}; r_a = {}'.format(s_a, r_a))
    return (n / s_len) * s_a + r_a

       
#print("{}".format(repeatedString('aba', 10)))
#print("{}".format(repeatedString('a', 10000)))

import unittest

class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdata = [
                    ('aba', 10, 7),
                    ('a', 10000, 10000)
                ]

        for s, n, a in tdata:
            r = repeatedString(s, n)
            self.assertEqual(a, r, 'Expr={}; Real={}'.format(a, r))


            
