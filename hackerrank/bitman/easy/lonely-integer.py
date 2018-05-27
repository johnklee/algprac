#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/lonely-integer/problem
'''

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    if len(a) == 1:
        return a[0]
    else:
        iset = set()
        for i in a:
            if i in iset:
                iset.remove(i)
            else:
                iset.add(i)

        return list(iset)[0]

print("{}".format(lonelyinteger([1])))
print("{}".format(lonelyinteger([0, 0, 1, 2, 1])))
