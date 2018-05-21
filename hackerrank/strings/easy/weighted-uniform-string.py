#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/weighted-uniform-string/problem
'''

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    answers = []
    uSet = set()
    pc = None
    av = None
    for i in range(len(s)):
        cc = ord(s[i]) - 96
        if pc is None:
            pc = cc
            uSet.add(cc)
            av = cc
            continue

        if pc == cc:
            av += cc
            uSet.add(av)
        else:
            pc = cc
            av = cc
            uSet.add(cc)

    for q in queries:
        if q in uSet:
            answers.append('Yes')
        else:
            answers.append('No')

    return answers


#queries = [1, 3, 12, 5, 9, 10]
#s = 'abccddde'
#for a in weightedUniformStrings(s, queries):
#    print(a)

import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        queries = [1, 3, 12, 5, 9, 10]
        s = 'abccddde'
        a = ''.join(weightedUniformStrings(s, queries))
        self.assertEqual('YesYesYesYesNoNo', a)
