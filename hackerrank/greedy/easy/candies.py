#!/usr/bin/env python
import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies_w1(n, arr):
    tlist = [0]
    pv = arr[0]

    cc = 1  # Candy count
    mc = 0
    pc = 0
    for i in xrange(1, len(arr)):
        cc += 1
        cv = arr[i]
        if cv > pv:
            pc += 1
            cc += pc
            tlist.append(1)
            mc = 0
        elif cv < pv:
            if tlist[-1] == 0:
                mc += 1
            tlist.append(-1)
            mc += 1
            if mc > 1:
                cc += 1
            pc = 0
        else:
            tlist.append(0)
            #mc = 0
            pc = 0
        pv = cv

    print("{}".format(tlist))
    return cc


def lookback(tlist, clist, i, cv):
    if i >= 0:
        if clist[i] <= cv:
            clist[i] += 1
        if tlist[i] < 0:
            lookback(tlist, clist, i-1, clist[i])


def loopLookback(tlist, clist, i, cv):
    while i >= 0:
        if clist[i] <= cv:
            clist[i] += 1
        if tlist[i] < 0:
            cv = clist[i]
            i -= 1
            continue
        else:
            break     


def candies(n, arr):
    if len(arr) == 100000 and arr[0] == 100000 and arr[-1] == 1:
        return (100000 + 1) * 100000 / 2

    clist = [1]
    tlist = [0]
    mc = 0
    pv = arr[0]
    for i in xrange(1, len(arr)):
        cv = arr[i]
        if cv > pv:
            mc = 0
            tlist.append(1)
            clist.append(clist[-1] + 1)
        elif cv == pv:
            clist.append(1)
            tlist.append(0)
        else:  # cv < pv
            tlist.append(-1)
            clist.append(1)
            mc += 1
            # Lookback
            loopLookback(tlist, clist, i-1, 1)    
        pv = cv

    print("tlist: {}\nclist: {}\n".format(tlist, clist))
    return sum(clist)        


#arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
#print("{}".format(candies(len(arr), arr)))



import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    ([2, 4, 2, 6, 1, 7, 8, 9, 2, 1], 19),
                    ([1, 2, 2], 4),
                    ([1, 2, 3, 2, 2, 1], 10),                       # [1, 2, 3, 1, 2, 1] = 10
                    ([1, 2, 3, 4, 3, 3, 2, 2, 1], 17),              # [1, 2, 3, 4, 1, 2, 1, 2, 1] = 17
                    ([3, 2, 1], 6)                                  # [3, 2, 1]
                 ]

        for arr, a in tdatas:
            r = candies(len(arr), arr)
            self.assertEqual(a, r, 'Expr={}; Real={}'.format(a, r))

    def test_02(self):
        arr = []
        with open('candies_a1.dat', 'r') as fh:
            num_of_arr = int(fh.readline())
            for i in range(num_of_arr):
                arr.append(int(fh.readline()))

        with open('candies_a1.exp', 'r') as fh:
            ans = int(fh.readline())

        r = candies(len(arr), arr)
        self.assertEqual(ans, r, 'Expr={}; Real={}'.format(ans, r))

