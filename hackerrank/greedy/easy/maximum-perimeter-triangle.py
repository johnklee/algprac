#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
'''

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sideSet = set()
    sideDict = {}
    mp = 0
    mp_sides = []

    # Collect data and check Equilateral
    for s in sticks:
        sideSet.add(s)
        if s in sideDict:
            if sideDict[s] + 1 >= 3 and  s * 3 > mp:
                mp = s * 3
                mp_sides = [s, s, s]
            else:
                sideDict[s] = sideDict[s] + 1
        else:
             sideDict[s] = 1

    sideSet = sorted(list(sideSet))
    
    # Check Isosceles
    for s, c in sideDict.items():
        if c >= 2:
            for i in range(sideSet.index(s), -1, -1):
                if sideSet[i] == s:
                    continue
                else:
                    c_mp = (s * 2 + sideSet[i])
                    if c_mp > mp:
                        mp = c_mp
                        mp_sides = [ sideSet[i], s, s]
                    break


    # Check Scalene
    sides = recvMP(sideSet, [], len(sideSet) - 1, mp)
    if sides:
        sides = sorted(sides)
        mp = sum(sides)
        mp_sides = sides     


    #mp_sides = map(str, mp_sides)

    if mp > 0:
        return mp_sides
    else:
        return [-1]


def recvMP(sideSet, sides, i, mp):
    if i < 0:
        return None
    else:
        if len(sides) == 2:
            for j in range(i, -1, -1):
                if abs(sides[1] - sides[0]) >= sideSet[j]:
                    return None
                else:
                    if sum(sides) + sideSet[j] > mp:
                        sides.append(sideSet[j])
                        return sides
                    else:
                        return None
            return None
        else:
            for j in range(i, 0, -1):
                nsides = []
                nsides.extend(sides)
                nsides.append(sideSet[j])
                usides = recvMP(sideSet, nsides, j - 1, mp)
                if usides:
                    return usides

            return None                



print("{}".format(maximumPerimeterTriangle([1, 1, 1, 3, 3])))
print("{}".format(maximumPerimeterTriangle([1, 2, 3])))
print("{}".format(maximumPerimeterTriangle([1, 1, 1, 2, 3, 5])))
print("{}".format(maximumPerimeterTriangle([1, 1, 1, 3, 4, 5])))
