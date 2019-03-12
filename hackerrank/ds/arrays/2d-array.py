#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/2d-array/problem
'''
import math
import os
import random
import re
import sys


def sumOfHG(arr, i, j):
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
           arr[i+1][j+1] + \
           arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    mGsum = -9 * 7

    for i in range(4):
        for j in range(4):
            cGsum = sumOfHG(arr, i, j)
            if cGsum > mGsum:
                mGsum = cGsum

    return mGsum


def readData(tn):
    fp = "{}.{}".format(os.path.basename(__file__).split('.')[0], tn)
    arr = []
    ans = 0
    with open(fp, 'r') as fh:
        ans = int(fh.readline())
        for line in fh:
            arr.append(map(lambda e: int(e.strip()), line.strip().split()))

    return ans, arr

#print("{}".format(hourglassSum(readData("td"))))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass


    def test_01(self):
        for i in [1, 2]:
            a, arr = readData('t{}'.format(i))
            r =  hourglassSum(arr)
            self.assertEqual(a, r, 'Expr={}; Real={}'.format(a, r))



