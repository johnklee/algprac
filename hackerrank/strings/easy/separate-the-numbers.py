#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/separate-the-numbers/problem
'''
import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s) <=1:
        return 'NO'
    elif s.startswith('0'):
        if check('0', s[1:]):
            return 'YES 0'
        else:
            return 'NO'
    else:
        #print('\tLimit={}'.format((len(s) + 1)/2))
        for i in range(1, (len(s) + 1)/2 + 1):
            #print('\tBegin={}...{}'.format(s[:i], i))
            if check(s[:i], s):
                return 'YES {}'.format(s[:i])

    return 'NO'


def check(sNum, s):
    #print('\tCheck {}...({})'.format(sNum, s))
    if len(s) == 0:
        return True
    elif len(sNum) > len(s):
        return False
    elif s.startswith(sNum):
        s = s[len(sNum):]
        nNum = str(int(sNum)+1)
        return check(nNum, s)
    else:
        return False


datas = ['8910', '8889']
for s in datas:
    print(separateNumbers(s))

import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        datas = ['1234', '91011', '99100', '101103', '010203', '13', '1']
        answr = ['YES 1', 'YES 9', 'YES 99', 'NO', 'NO', 'NO', 'NO']
        for i in range(len(datas)):
            self.assertEqual(separateNumbers(datas[i]), answr[i])

    def test_02(self):
        datas = ['1', '2', '33', '4445', '8889', '8910'] 
        answr = ['NO', 'NO', 'NO', 'YES 44','YES 88', 'YES 8']
        for i in range(len(datas)):
            self.assertEqual(separateNumbers(datas[i]), answr[i])
