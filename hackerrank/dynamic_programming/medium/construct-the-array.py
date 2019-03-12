#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/construct-the-array/problem
'''

import math
import os
import random
import re
import sys


def countArray(n, k, x):
    if n == 3:
        return x - len(set([1, x]))
    else:
        cnt = 0
        # todo
        return cnt



# Complete the countArray function below.
def countArray_v1(n, k, x):
    # Return the number of ways to fill in the array.
    return recCntAry(2, 1, n, k, x)

cacheDict = {}
def recCntAry(cn, pv, n, k, x):
    if cn + 1 == n:
        key = (pv==x, n - cn)
        if key in cacheDict:
            return cacheDict[key]
        # The post before the last position
        cnt = 0
        for i in xrange(1, k+1):
            if i == pv or i == x:
                continue 
            cnt += recCntAry(cn + 1, i, n ,k, x)
            #print('\tCheck {} at cn={}...'.format(i, cn))
        #print("Got {} at cn={}".format(cnt, cn))        
        cacheDict[key] = cnt
        #print("cache {}={}".format(key, cnt))
        return cnt
    elif cn == n:
        return 1
    elif cn < n:
        key = (pv==x, n - cn)
        if key in cacheDict:
            return cacheDict[key]
        
        cnt = 0
        for i in xrange(1, k+1):
            if i == pv:
                continue
            cnt += recCntAry(cn + 1, i, n ,k, x)
            #print('\tCheck {} at cn={}...'.format(i, cn))
        #print("Got {} at cn={}".format(cnt, cn))
        cacheDict[key] = cnt
        #print("cache {}={}".format(key, cnt))
        return cnt

for i in range(3, 100):
    print("i={}: {}".format(i, countArray_v1(i, 3, 2)))

