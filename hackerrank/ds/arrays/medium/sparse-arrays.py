#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/sparse-arrays/problem
'''
import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    caches = {}
    result = []
    strings_len_dict = {}
    for i in xrange(len(strings)):
        s = strings[i]
        s_len = len(s)
        if s_len in strings_len_dict:
            s_dict = strings_len_dict[s_len]
            s_dict[s] = s_dict.get(s, 0) + 1
        else:
            strings_len_dict[s_len] = {s:1}

    for q in queries:
        c = caches.get(q, None)
        if c:
            result.append(c)
        else:
            q_len = len(q)
            s_dict = strings_len_dict.get(q_len, None)
            if s_dict:
                result.append(s_dict.get(q, 0))
            else:
                result.append(0)

    return tuple(result)


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass


    def test_01(self):
        tdatas = [
                    (('ab', 'ab', 'abc'), ('ab', 'abc', 'bc'), (2, 1, 0)),
                    (('def', 'de', 'fgh'), ('de', 'lmn', 'fgh'), (1, 0, 1))
                 ]
        for strings, queries, a in tdatas:
            r = matchingStrings(strings, queries)
            self.assertEqual(a, r, 'Expr: {}; Real: {}'.format(a, r))


