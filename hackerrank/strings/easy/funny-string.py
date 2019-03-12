#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/funny-string/problem
'''

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    if len(s) <= 2:
        return 'Funny'

    plist = []
    rlist = []
    tc = s[0]
    for i in xrange(1, len(s)):
        cc = s[i]
        d = abs(ord(cc) - ord(tc))
        plist.append(d)
        rlist.insert(0, d)
        tc = cc

    plist = map(str, plist)
    rlist = map(str, rlist)
    #print('plist={}; rlist={}'.format(plist, rlist))
    return 'Funny' if ','.join(plist) == ','.join(rlist) else 'Not Funny'


print("{}".format(funnyString('abc')))
print("{}".format(funnyString('acxz')))
print("{}".format(funnyString('bcxz')))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [ 
                    ('abc', 'Funny'),
                    ('acxz', 'Funny'),
                    ('bcxz', 'Not Funny'),
                    ('ab', 'Funny'),
                    ('abfjk', 'Funny')
                 ]

        for dat, a in tdatas:
            r = funnyString(dat)
            self.assertEqual(a, r, '{}: Expr={}; Real={}'.format(dat, a, r))
