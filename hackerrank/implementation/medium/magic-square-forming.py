#!/usr/bin/env python

import math
import os
import random
import re
import sys
from pprint import pprint

magic_squares = [[[2, 7, 6], [9, 5, 1], [4, 3, 8]],
[[2, 9, 4], [7, 5, 3], [6, 1, 8]],
[[4, 3, 8], [9, 5, 1], [2, 7, 6]],
[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
[[6, 1, 8], [7, 5, 3], [2, 9, 4]],
[[6, 7, 2], [1, 5, 9], [8, 3, 4]],
[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
[[8, 3, 4], [1, 5, 9], [6, 7, 2]]]

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    mc = -1
    for ms in magic_squares:
        cs = cost(ms, s)
        if mc < 0 or mc > cs:
            mc = cs

    return mc

def cost(ms, os):
    c = 0
    for i in range(3):
        for j in range(3):
            c += abs(ms[i][j] - os[i][j])

    return c   

def rsum(squares, ri):
    return sum(squares[ri])

def csum(squares, ci):
    return sum(map(lambda e: e[ci], squares))

def isMagic(squares):
    if squares[0][0] + squares[1][1] + squares[2][2] !=15:
        return False

    if squares[0][2] + squares[1][1] + squares[2][0] !=15:
        return False

    for i in range(3):
        if rsum(squares, i) != 15 or csum(squares, i) != 15:
            return False    

    return True

def l2s(alist):
    squares = []
    row = []
    for i in range(9):
        row.append(alist[i])
        if (i + 1) % 3 == 0:
            squares.append(row)
            row = []

    return squares

def coltMS():
    r'''
    Generate magic square collection
    ''' 
    magic_squares = []   
    all_squares_as_list = []
    perm([], all_squares_as_list)
    for alist in all_squares_as_list:
        square = l2s(alist)
        #pprint(square)
        if isMagic(square):
            magic_squares.append(square)

    return magic_squares


def perm(clist, tlist):
        if len(clist) == 9:
            tlist.append(clist)
        else:
            for i in range(1, 10):
                if i not in clist:
                    nlist = []
                    nlist.extend(clist)
                    nlist.append(i)
                    perm(nlist, tlist)


#magic_squares = coltMS()
#print('Total {} magic squares being collected:'.format(len(magic_squares)))
#for msquare in magic_squares:
#    pprint(msquare)
data = [[5,3,4],[1,5,8],[6,4,2]]
print("{}".format(formingMagicSquare(data)))
