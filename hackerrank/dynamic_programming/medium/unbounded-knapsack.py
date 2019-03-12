#!/usr/bin/env python3
r'''
https://www.hackerrank.com/challenges/unbounded-knapsack/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''
import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    arr_set = sorted(list(set(list(filter(lambda e: e<=k, arr)))), reverse=True)
    
    # Short cut
    if 1 in arr_set or k in arr_set:
        return k
    
    # Dividable
    cloest_to_k = 0
    for i in range(len(arr_set)):
        v = arr_set[i]
        if k % v == 0:
            return k
        else:             
            tk = v
            rv = k - tk
            aarr = arr_set
            rlist = list(filter(lambda e: e<=rv, aarr))
            #print('Handle tk={}; rv={}; aarr={}; rlist={}'.format(tk, rv, aarr, rlist))
            while len(rlist) > 0:
                tk += rlist[0]
                rv = k - tk
                rlist = list(filter(lambda e: e<=rv, aarr))
            
            if tk > cloest_to_k:
                cloest_to_k = tk
                
    return cloest_to_k

print(unboundedKnapsack(13, [3, 10, 4]))

import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass


    def read_tc(self, tn):
        module_name = __file__.split('.')[0]
        test_case_fname = "{}.t{}".format(module_name, tn)
        answer_fname = "{}.a{}".format(module_name, tn)
        test_cases = []
        answers = []
        with open(test_case_fname, 'r') as fh:
            num_of_case = int(fh.readline())
            for i in range(num_of_case):
                size_of_ary, k = fh.readline().split()
                array = list(map(int, fh.readline().split()))
                test_cases.append((int(k), array))

        with open(answer_fname, 'r') as fh:
            for line in fh:
                answers.append(int(line))

        return (test_cases, answers)

    def test_01(self):
        test_cases, answers = self.read_tc(1)
        for tup, anw in zip(test_cases, answers):
            k, array = tup
            rel = unboundedKnapsack(k, array)
            self.assertEquals(anw, rel, "k={}; array={}; exp={}; rel={}".format(k, array, anw, rel))

    def test_04(self):
        test_cases, answers = self.read_tc(4)
        for tup, anw in zip(test_cases, answers):
            k, array = tup
            rel = unboundedKnapsack(k, array)
            self.assertEquals(anw, rel, "k={}; array={}; exp={}; rel={}".format(k, array, anw, rel))

    def test_10(self):
        test_cases, answers = self.read_tc(10)
        for tup, anw in zip(test_cases, answers):
            k, array = tup
            rel = unboundedKnapsack(k, array)
            self.assertEquals(anw, rel, "k={}; array={}; exp={}; rel={}".format(k, array, anw, rel))
