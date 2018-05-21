#!/usr/bin/env python
import math
import os
import random
import re
import sys


# Complete the pangrams function below.
def pangrams(s):
    s = s.lower().replace(' ', '')
    if len(s) < 26:
        return 'not pangram'
    else:
        cs = set()
        for c in s:
            cs.add(c)
        return 'pangram' if len(cs) == 26 else 'not pangram'



print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('We promptly judged antique ivory buckles for the prize'))


import unittest

class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        self.assertEqual('pangram', pangrams('We promptly judged antique ivory buckles for the next prize'))
        self.assertEqual('not pangram', pangrams('We promptly judged antique ivory buckles for the prize'))
        
