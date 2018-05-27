#!/usr/bin/env python
import math
import os
import random
import re
import sys

r'''
https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
'''

def covg(i, aset, k):
    hits = []
    for v in range(i-k, i+k+1):
        if v in aset:
            hits.append(v)
    #print('\t{} has {} hit!'.format(i, len(hits)))
    return hits

def hackerlandRadioTransmitters(x, k):
    #print("Handle {}...{}".format(x, k))
    aset = set()
    for i in x:
        aset.add(i)

    tc = 0    
    while len(aset) > 0:
        phits = None
        pi = None
        for i in aset:
            hits = covg(i, aset, k)
            if phits == None or len(hits) >= len(phits):
                phits = hits
                pi = i
            #else:
    
        #print('C={}...{}|{}'.format(pi, len(phits), tc+1))
        tc += 1
        for j in phits:
            aset.remove(j)

        #if len(phits) > 0:
        #    print('*C={}...{}'.format(pi, len(phits)))
        #    for j in phits:
        #        aset.remove(j)
        #    tc += 1
        #print('Rest={}'.format(list(aset)))
    return tc        


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters_v1(x, k):
    hp_dict = {}
    cv_dict = {}
    for hp in x:
        hp_dict[hp] = hp_dict.get(hp, 0) + 1

    tc = 0        
    while len(hp_dict) > 0:
        mc = 0
        mset = None
        for hp in hp_dict.keys():
            tset = set()
            tmc = 0
            #print('Check range({},{}).. k={}; hp={}'.format(hp-k, hp+k, k, hp))
            for i in range(hp-k, hp+k+1):
                if i in hp_dict:
                    tset.add(i)
                    tmc += hp_dict.get(i)

            if tmc > mc:
                mc = tmc
                mset = tset

        #print('Remove {}'.format(mset))
        for j in mset:
            hp_dict.pop(j, None)    
        tc += 1
        if len(hp_dict) == 1:
            tc += 1
            break

    return tc


#print("{}".format(hackerlandRadioTransmitters([1, 2, 3, 4, 5], 1)))
#print("{}".format(hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2)))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    ([1, 2, 3, 4, 5], 1, 2),
                    ([7, 2, 4, 6, 5, 9, 12, 11], 2, 3),
                    ([1, 2, 3, 4, 5, 6, 7, 11], 3, 2),
                    ([1, 2, 3, 7, 8, 9, 13], 1, 3)
                 ]

        for x, k, a in tdatas:
            ti = hackerlandRadioTransmitters(x, k)
            self.assertEqual(a, ti, 'Expect={};Real={} for {}'.format(a, ti, x))

    def test_02(self):
        tid = ['1']
        tdatas = []
        for id in tid:
            with open('hackerland-radio-transmitters.t{}'.format(id), 'r') as fh:
                num, k = fh.readline().split(' ')
                x = fh.readline().strip().split(' ')
                self.assertEqual(int(num), len(x), 'Expect to have {} hp; Real = {} in ID={}'.format(num, len(x), id))
                x = map(int, x)
                with open('hackerland-radio-transmitters.a{}'.format(id), 'r') as fh2:
                    a = int(fh2.readline())
                    tdatas.append((x, int(k), a))

        for x, k, a in tdatas:
            ti = hackerlandRadioTransmitters(x, k)
            self.assertEqual(a, ti, 'Expect={};Real={} for {}'.format(a, ti, x))
