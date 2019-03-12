#!/usr/bin/env python3
r'''
https://www.hackerrank.com/challenges/red-john-is-back/problem
'''
import math
import os
import random
import re
import sys

primes = [2, 3, 5, 7]

def isPrime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False

    return True

def look4Prime(n):
    if primes[-1] < n:
        # Extend the primes
        for i in range(primes[-1]+1, n+1):
            if isPrime(i):
                primes.append(i)

    return len(list(filter(lambda e: e <=n, primes)))


perm_caches = {}
def permNum(bs, slot):
    global perm_caches
    num = perm_caches.get((bs, slot), None)
    if num is None:
        if slot == 2:
            perm_caches[(bs, slot)] = bs + 1
            return bs + 1
        else:
            num = 0
            for i in range(bs+1):
                num += permNum(i, slot-1)

            perm_caches[(bs, slot)] = num
    
    return num 

# Complete the redJohn function below.
def redJohn(n):
    if n <= 4:
        return 0   
    else:
        cfg_num = 1        
        for i in range(1, int(n/4)+1):
            vert_cnt = i * 4
            hort_cnt = n - vert_cnt
            print('v={}; h={}'.format(vert_cnt, hort_cnt))
            cfg_num += permNum(hort_cnt, i + 1)
            

        print('\t{}->{}'.format(n, cfg_num))    
        return look4Prime(cfg_num)

for i in [1, 7, 34]:
    print("{}\t{}".format(i, redJohn(i)))


