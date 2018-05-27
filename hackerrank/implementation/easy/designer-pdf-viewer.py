#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
'''
import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxHeight = 0
    for i in range(len(word)):
        ch = h[ord(word[i]) - 97]
        if ch > maxHeight:
            maxHeight = ch

    return maxHeight * len(word)


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        self.assertEqual(9, designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc'))
        self.assertEqual(28, designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], 'zaba'))

