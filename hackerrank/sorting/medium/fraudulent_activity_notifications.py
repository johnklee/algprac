#!/usr/local/bin/python3
r'''
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
'''
import math
import os
import random
import re
import sys
from queue import Queue

class EM:
    def __init__(self, d):
        self.d = d
        self.is_odd = d % 2 == 1
        self.mp = int(math.ceil(self.d / 2))
        self.q = Queue(-1)
        self.c = [0] * 201

    def append(self, v):
        self.c[v] += 1
        self.q.put(v)
        if self.q.qsize() == self.d:
            m = self.mean()
            self.c[self.q.get()] -= 1
            return m
        else:
            return None

    def mean(self):            
        c = 0
        for i in range(200+1):
            c += self.c[i]
            if c >= self.mp:
                if self.is_odd:
                    return i
                else:
                    if c > self.mp:
                        return i
                    else:
                        for j in range(i + 1, 200+1):
                            if self.c[j] > 0:
                                return (i + j) / 2

        print("Something wrong: self.mp={}; c={}; self.c={}".format(self.mp, c, self.c))

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    wc = 0
    em = EM(d)
    pm = None
    for e in expenditure:
        if pm:
            print("pm={}; e={}".format(pm, e))
            if e >= 2 * pm:
                wc += 1
        
        pm = em.append(e)
        print("e={} -> pm={}".format(e, pm))

    return wc


import unittest


class FAT(unittest.TestCase):
    def test_d1(self):
        for d, expd, a in [
                            (5, [2, 3, 4, 2, 3, 6, 8, 4, 5], 2),
                            (4, [1, 2, 3, 4, 4], 0)
                          ]:
            r = activityNotifications(expd, d)
            self.assertEqual(a, r, 'exp={} with E={}; R={}'.format(expd, a, r))
