#!/usr/bin/pyhton3
r'''
https://www.hackerrank.com/challenges/palindrome-index/problem
'''
import math
import os
import random
import re
import sys

def is_pali(s):
    s_len = len(s)
    if s_len <= 1:
        return True
    else:
        for i in range(int(s_len/2)):
            if s[i] != s[-(i+1)]:
                return False

        return True

def ds(s, i):
    slist = list(s)
    del slist[i]
    return ''.join(slist)

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if is_pali(s):
        return -1
    else:
        for i in range(len(s)):
            if s[i] != s[-(i + 1)]:
                if is_pali(ds(s, i)):
                    return i
                else:
                    return len(s) - 1 - i


import unittest


print(__file__)

class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def read_tc(self, tn):
        module_name = __file__.split('.')[0]
        test_case_fname = "{}.t{}".format(module_name, tn)
        answer_fname = "{}.a{}".format(module_name, tn)
        test_case_list = []
        answer_list = []
        with open(test_case_fname, 'r') as fh:
            fh.readline()
            for line in fh:
                line = line.strip()
                test_case_list.append(line)

        with open(answer_fname, 'r') as fh:
            for line in fh:
                line = line.strip()
                answer_list.append(int(line))

        return (test_case_list, answer_list)

    def test_00(self):
        test_cases = ['aaab', 'baa', 'aaa', 'abaa']
        answers = [3, 0, -1, 1]
        for t, a in zip(test_cases, answers):
            r = palindromeIndex(t)
            self.assertEqual(a, r, 'T={}; Expr={}; Real={}'.format(t, a, r))

    def test_05(self):
        test_cases, answers = self.read_tc(5)
        for t, a in zip(test_cases, answers):
            r = palindromeIndex(t)
            self.assertEqual(a, r, 'T={}; Expr={}; Real={}'.format(t, a, r))
