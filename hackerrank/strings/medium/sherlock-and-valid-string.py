#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
'''
import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    r'''
    Be valid if it all characters of the string appear the same number of times
    '''
    # short cut
    if len(s) <= 1:
        return 'YES'

    cfDict = {}
    for c in s:
        cfDict[c] = cfDict.get(c, 0) + 1

    fcDict = {}
    for c, f in cfDict.items():
        if f in fcDict:
            fcDict[f].append(c)        
        else:
            if len(fcDict) > 1:
                return 'NO'
            fcDict[f] = [c]

    print("{}:{}".format(s, fcDict))
    if len(fcDict) == 1:
        return 'YES'
    elif len(fcDict) > 2:
        return 'NO'
    else:
        fitems = sorted(fcDict.items(), key=lambda t:t[0])
        if fitems[0][0] + 1 == fitems[1][0] and len(fitems[1][1]) == 1:
            return 'YES'
        elif fitems[0][0] == 1 and len(fitems[0][1]) == 1:
            return 'YES'
        else:
            return 'NO'



#print("{}".format(isValid('abc')))
#print("{}".format(isValid('abcc')))
#print("{}".format(isValid('aabbcd')))
#print("{}".format(isValid('aabbccddeefghi')))

import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    ('abc', 'YES'),
                    ('abcc', 'YES'),
                    ('aabbcd', 'NO'),
                    ('aaabbbbccc', 'YES'),
                    ('aabbccddeefghi', 'NO'),
                    ('aabbccddeei', 'YES'),
                    ('abccd', 'YES'),
                    ('a', 'YES'),
                    ('', 'YES')
                 ]

        for data, a in tdatas:
            r = isValid(data)
            self.assertEqual(a, r, 'Expr={}; Real={}'.format(a, r))
