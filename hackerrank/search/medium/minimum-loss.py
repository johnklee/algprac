#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/minimum-loss/problem
Fail in time complexity
'''
import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss_v1(price):
    cDict = {}
    cx = sys.maxsize
    cDict[price[0]] = cx
    mc = max(price)
    for i in xrange(1, len(price)):
        cp = price[i]
        for p, c in cDict.items():
            cc = p - cp
            if cc == 1:
                return 1
            elif cc > 0 and cc < c:
                #print('Local MC={}...({},{},{})'.format(cc, p, cp, mc))
                cDict[p] = cc
                if cc < mc:
                    #print('\tUpdate mc={}'.format(cc))
                    mc = cc

        if cp not in cDict:
            cDict[cp] = sys.maxsize
            #print('\tNew P={}'.format(cp))

        # Clean up actions
        if len(cDict) > 1000 and mc < 10:
            pop_list = []
            for p, c in cDict.items():
                if c > mc:
                    isHit=False
                    for ti in range(1, mc):
                        if (p + ti) in price[i:]:
                            if ti == 1:
                                return 1
                            else:
                                isHit = True
                                break
                    if not isHit:
                        pop_list.append(p)

            # Clean key
            for pv in pop_list:
                cDict.pop(pv, None)

    return mc


def minimumLoss(price):
    mc = sys.maxsize
    dnSet = set()
    for i in xrange(len(price)-1):
        p = price[i]
        if p in dnSet:
            continue
        for j in xrange(i+1, len(price)):
            cc = p - price[j]
            if cc == 1:
                return 1
            elif cc > 0 and cc < mc:
                mc = cc
        dnSet.add(p)

    return mc            


print("Got {}".format(minimumLoss([5, 10, 3])))
print("Got {}".format(minimumLoss([20, 7, 8, 2, 5])))

import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    ([5, 10, 3], 2),
                    ([20, 7, 8, 2, 5], 2)
                 ]

        for prices, a in tdatas:
            ml = minimumLoss(prices)
            self.assertEqual(a, ml, 'Exp={}; Rel={}'.format(a, ml))
