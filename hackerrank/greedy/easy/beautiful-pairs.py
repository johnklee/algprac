#!/usr/bin/env python3
r'''
https://www.hackerrank.com/challenges/beautiful-pairs/problem
'''
import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    aset = set(A)
    lset = set()
    rset = set()

    bp_list = []
    sdict = {}
    for i in range(len(A)):
        av = A[i]
        bi_list = sdict.get(av, None)
        if bi_list is None:
            bi_list = [i for i, bv in enumerate(B) if bv == av]
            sdict[av] = bi_list

        for bi in bi_list:
            if bi not in rset:
                bp_list.append((i, bi))
                lset.add(i)
                rset.add(bi)
                break

    bp_len = len(bp_list)
    if bp_len < len(aset):
        return bp_len + 1
    else:
        return bp_len

import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass


    def read_tc(self, tn):
        module_name = __file__.split('.')[0]
        test_case_fname = "{}.t{}".format(module_name, tn)
        answer_fname = "{}.a{}".format(module_name, tn)        
        with open(test_case_fname, 'r') as fh:
            fh.readline()
            A = list(map(int, fh.readline().split()))
            B = list(map(int, fh.readline().split()))

        with open(answer_fname, 'r') as fh:
            answer = int(fh.readline())

        return (A, B, answer)

    def test_01(self):
        A, B, ans = self.read_tc(1)
        rel = beautifulPairs(A, B)
        self.assertEqual(ans, rel, 'Exp={}; Real={}'.format(ans, rel))

    def test_04(self):
        A, B, ans = self.read_tc(4)
        rel = beautifulPairs(A, B)
        self.assertEqual(ans, rel, 'Exp={}; Real={}'.format(ans, rel))
