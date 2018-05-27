#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/marcs-cakewalk/problem
'''

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    sorted_calorie = sorted(calorie, reverse=True)

    sum_miles = 0
    for i in range(len(sorted_calorie)):
        sum_miles += math.pow(2, i) * sorted_calorie[i]

    return int(sum_miles)


#print("{}".format(marcsCakewalk([1, 3, 2])))
#print("{}".format(marcsCakewalk([5, 10, 7])))

import unittest

class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    ([1, 3, 2], 11),
                    ([5, 10, 7], 44)
                 ]

        for calorie, a in tdatas:
            r = marcsCakewalk(calorie)
            self.assertEqual(a, r, 'Expect={}; Real={}'.format(a, r))
