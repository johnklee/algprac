#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/grid-challenge/problem
'''
import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    plist = None
    for rstr in grid:
        clist = []
        for c in rstr:
            clist.append(c)

        clist = sorted(clist)
        if plist is not None:
            for i in range(len(clist)):
                if plist[i] > clist[i]:
                    return 'NO'
        plist = clist

    return 'YES'


grid = ['ebacd', 'fghij', 'olmkn',  'trpqs', 'xywuv' ]
print("{}".format(gridChallenge(grid)))
