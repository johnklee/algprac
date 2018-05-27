#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/the-hurdle-race/problem
'''
import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_dose = 0
    for h in height:
        dose = h - k
        if dose > 0 and dose > max_dose:
            max_dose = dose

    return max_dose


import unittest

class FAT(unittest.TestCase):
    def setUp(self):
        pass


    def test_01(self):
        self.assertEqual(2, hurdleRace(4, [1, 6, 3, 5, 2]))
        self.assertEqual(0, hurdleRace(7, [2, 5, 4, 5, 2]))
