#!/usr/local/bin/python3
r'''
https://www.youtube.com/watch?v=CoI4S7z1E1Y&index=75&list=WL
'''
import math
from random import random as rdm


def randi(n):
    r'''
    Return a number in range [0, n) randomly
    '''
    return int(math.floor(rdm() * n))


def swap(n, m, alist):
    r'''
    Swap the given position n, m from the given list
    '''
    alist[n], alist[m] = alist[m], alist[n]


def reorder(alist):
    r'''
    Reorder the given list in O(n) time complexity inplace.
    '''
    for i in range(len(alist)-1, 0, -1):
        ri = randi(i+1)
        if ri != i:
            swap(i, ri, alist)

    return alist
