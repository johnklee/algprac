#!/usr/bin/env python
import math
import os
import random
import re
import sys

r'''
https://www.hackerrank.com/challenges/coin-change/problem
'''

# Complete the getWays function below.
def getWays(n, c):
    r'''
    @param n(int):
        n unit
    @param c(list):
        values of each coin
    '''
    #return rgetWays(n, c)
    return dp_getWays(n, c)

       
def dp_getWays(n, c):
    vlist = []
    ''' selected coin value list '''
    plist = []
    ''' coin position list '''
    ac = sorted(filter(lambda e: e<=n, c))
    ''' coin value list '''
    solutions = 0
    ''' list to hold coin change '''
    
    if len(ac) == 0:
        return 0
    else:
        sum = 0
        cp = 0
        vlist.append(ac[cp])
        plist.append(cp)
        while len(plist) > 0:
            if sum < n:
                sum += ac[cp]
                plist.append(cp)
                vlist.append(ac[cp])
            elif sum >= n:
                if sum == n:
                    #nlist = []
                    #nlist.extend(vlist)
                    #solutions.append(nlist)
                    solutions += 1
                    print("Solution={}...".format(solutions))
                    #print('Got solution {} for {}'.format(nlist, n))

                # Backward-1 
                sum -= vlist[-1]
                vlist = vlist[:-1]
                plist = plist[:-1]

                # Backward-2
                try:
                    pp = plist[-1]
                    while pp+1 >= len(ac):
                        sum -= vlist[-1]
                        vlist = vlist[:-1]
                        plist = plist[:-1]
                        pp = plist[-1]
                    cp = pp + 1
                    sum -= vlist[-1]
                    vlist = vlist[:-1]
                    plist = plist[:-1]
                except:
                    #print('Done!') 
                    break

    return solutions

# Recursive version - Complete the getWays function below.
def rgetWays(n, c):
    r'''
    @param n(int):
        n unit
    @param c(list):
        values of each coin
    '''
    # Select all coin values less or equal to the 'n'
    ac = sorted(filter(lambda e: e<=n, c))
    solutions = []
    _recvGetWays(n, ac, [], solutions)
    return len(solutions)
    
def _recvGetWays(n, c, clist, solutions):
    if n == 0:
        nlist = []
        nlist.extend(clist)
        solutions.append(nlist)
    else:
        cc = filter(lambda e: e<=n, c)
        if len(clist) > 0:
            cc = filter(lambda e: e>=clist[-1], cc)
        for e in cc:
            if e <= n:
                clist.append(e)
                _recvGetWays(n-e, c, clist, solutions)
                del clist[-1]


#solutions = getWays(4, [3, 1, 2])
#print('Total {} solutions:'.format(len(solutions)))
#for cc in solutions:
#    print('\t{}'.format(cc))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    @staticmethod
    def readData(fn):
        with open(fn, 'r') as fh:
            n, l = map(int, fh.readline().split())
            clist = map(int, fh.readline().split())
            return (n, clist)

    @staticmethod
    def readExp(fn):
        with open(fn, 'r') as fh:
            return int(fh.readline().strip())

    def test_01(self):
        self.assertEquals(4, getWays(4, [3, 1, 2]))
        self.assertEquals(5, getWays(10, [2, 5, 3, 6]))
        self.assertEquals(3, getWays(3, [8, 3, 1, 2]))

    def test_02(self):
        n, clist = self.readData('coin_change_t1.data')
        exp = self.readExp('coin_change_t1.exp')
        rel = getWays(n, clist)
        self.assertEquals(exp, rel, 'Expect: {}; Real: {}'.format(exp, rel))


n, clist = FAT.readData('coin_change_t1.data')
exp = FAT.readExp('coin_change_t1.exp')
print('Handle n={}; clist={}; with exp={}...'.format(n, clist, exp))
rel = getWays(n, clist) 
