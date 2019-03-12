#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''
import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard_v1(scores, alice):
    results = []
    pv = scores[0]
    ranks = [pv]
    for i in range(1, len(scores)):
        cv = scores[i]
        if cv != pv:
            ranks.append(cv)
        pv = cv

    pi = len(ranks)
    for s in alice:
        if s < ranks[-1]:
            results.append(len(ranks) + 1)
        elif s >= ranks[0]:
            results.append(1)
        else:
            for i in range(1, len(ranks)):
                rs = ranks[i]
                if rs == s:
                    results.append(i+1)
                    pi = i 
                    break
                elif rs > s:
                    continue
                else:  # rs < s
                    results.append(i+1)
                    break

    return tuple(results)


def climbingLeaderboard(scores, alice):
    print("scores={}".format(scores))
    print("alice={}".format(alice))
    results = []
    # Look for start
    pi = 1
    ii = None
    pv = scores[0]
    for i in xrange(1, len(scores)):
        cv = scores[i]
        if cv > alice[0]:
            if pv != cv:
                pv = cv
                pi += 1
            continue
        elif cv <= alice[0]:
            if pv != cv:
                pv = cv
                pi += 1
            ii = i
            break

    if ii is None:
        ii = len(scores) - 1

    if alice[0] < scores[-1]:
        pi += 1
    results.append(pi)

    print('{} @ rank {}...(i={},{})'.format(alice[0], pi, ii, scores[ii]))

    ai = 1
    while pi > 1 and ai < len(alice):
        for i in xrange(ii, -1, -1):
            cv = scores[i]
            if cv < alice[ai]:
                if pv != cv:
                    pv = cv
                    pi -= 1
                continue
            elif cv >= alice[ai]:
                if pv != cv:
                    pv = cv
                    pi -= 1
                print('{} @ rank {}...(i={},{})'.format(alice[ai], pi, i, cv))
                ii = i
                ai += 1
                results.append(pi)
                break

        print("i={}; pi={}".format(i, pi))
        if i == 0 and alice[ai] >= scores[0]:
            results.append(1)
            break 
    return results


print("{}".format(climbingLeaderboard([100, 50, 40, 10, 5], [1, 20, 90, 90, 110])))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    ([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120], (6, 4, 2, 1)),
                    ([100, 50, 40, 10, 5], [1, 20, 90, 110], (6, 4, 2, 1)),
                    ([100, 50, 40, 10, 5], [1, 20, 90, 90, 110], (6, 4, 2, 2, 1))
                 ]

        for scores, alice, a in tdatas:
            r = climbingLeaderboard(scores, alice)
            self.assertEqual(a, r, "Expr={}; Real={}".format(a, r))
