#!/usr/bin/env python
import math
import os
import random
import re
import sys

def comm(n, k):
    r'''
    Calculate C(n, k) which evaluates the number of different 
    combinations of n items taken k at a time.
    '''
    if k == 1:
        return n
    elif n == k or k == 0:
        return 1
    else:
        return comm(n-1, k-1) + comm(n-1, k)


def ass(S):
    r'''
    Find all sub set of given set S

    By mathematical induction, it can be shown that if S has n elements, then the number of subsets 
    from its power set is 2^n. For instance, assume S={1,2,3}. The power set has 2^3=8 subsets.

    @see:
        http://localhost/jforum/posts/list/1452.page
    '''
    if len(S) == 1:
        return [(), tuple(S)]
    elif len(S) == 0:
        return [()]
    else:
        all_sub_set = [()]
        _ass(S, 0, [], all_sub_set)
        return all_sub_set

def a2s(cs, e):
    ts = []
    ts.extend(cs)
    ts.append(e)
    return ts

def _ass(S, p, cs, ss):
    if p >= len(S):
        return 
    for i in range(p, len(S)):
        e = S[i]
        ns = a2s(cs, e)
        ss.append(tuple(ns))
        _ass(S, i+1, ns, ss)


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_api_comm(self):        
        self.assertEqual(4, comm(4, 1))
        self.assertEqual(6, comm(4, 2))
        self.assertEqual(4, comm(4, 3))
        self.assertEqual(1, comm(4, 4))

    def test_api_ass(self):
        self.assertEqual(8, len(ass([1, 2, 3])))
        self.assertEqual(16, len(ass([1, 2, 3, 4])))


#########################
# Testing API:ass
#########################
#S = [1, 2, 3, 4]
#all_sub_set = ass(S)
#print('Total {} sub set being returned:'.format(len(all_sub_set)))
#for ss in all_sub_set:
#    print(ss)
