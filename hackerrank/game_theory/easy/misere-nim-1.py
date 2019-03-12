#!/usr/bin/env python3
r'''
https://www.hackerrank.com/challenges/misere-nim-1/problem
'''
import math
import os
import random
import re
import sys


def winer(rst):
    if rst:
        return 'First'
    else:
        return 'Second'


# Complete the misereNim function below.
def misereNim(s):
    # In a single pile, if more than one stones exist then first player will
    # always win by leaving the last stone for second player to pick up
    if len(s) == 1:
        return winer(s[0] > 1)

    totalStones = 0
    xorValue = 0

    for i in range(0, len(s)):
        totalStones += s[i]
        xorValue ^= s[i]

    r'''
    If sum of all stones equals the total piles, all piles have a single (1)
    stone. For even number of piles, first player will always win.
    '''
    if totalStones == len(s):
        return winer(totalStones % 2 == 0)

    r'''
    For all other cases, the xor value determines winner. If xor value = 0,
    then second player will always win as all piles (stones) can be paired.
    '''
    print('xorValue={}'.format(xorValue))
    return winer(xorValue > 0)



print("{}".format(misereNim([2, 1, 3])))
