#!/usr/bin/env python3
import math
import os
import random
import re
import sys

def swap(w, i, j):
    w[i], w[j] = w[j], w[i]

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    #print('w={}'.format(w))
    wi = list(map(lambda e: ord(e), w))
    wi_len = len(wi)
    
    for i in range(1, wi_len):
        #print("Check i={}:{}".format(-i, w[-i]))
        for j in range(i+1, wi_len+1):
            #print("\tj={}:{}".format(-j, w[-j]))
            if wi[-j] < wi[-i]:
                swap(wi, -i, -j)
                bt_list = wi[-j+1:]
                hd_list = wi[:-j+1]
                #print('\tbt_list={}'.format(bt_list))
                #print('\thd_list={}'.format(hd_list))
                bt_list = sorted(bt_list)
                return ''.join(list(map(chr, hd_list+bt_list)))
        
    return 'no answer'


def loadTC(n):
    tc_list = []
    aw_list = []
    pn = __file__.split('.')[0]
    with open('{}.t{}'.format(pn, n), 'r') as fh:
        fh.readline()
        for line in fh:
            line = line.strip()
            tc_list.append(line)

    with open('{}.a{}'.format(pn, n), 'r') as fh:
        for line in fh:
            line = line.strip()
            aw_list.append(line)

    return (tc_list, aw_list)


# Test
#print("{}".format(biggerIsGreater('dkhc')))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_0(self):
        tc_list, aw_list = loadTC(0)
        for tc, aw in zip(tc_list, aw_list):
            rel = biggerIsGreater(tc)
            self.assertEqual(aw, rel, 'TC={}: Exp={}; Rel={}'.format(tc, aw, rel))
