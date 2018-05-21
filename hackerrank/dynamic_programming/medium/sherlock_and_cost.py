#!/usr/bin/env python
import math
import os
import random
import re
import sys


# Complete the cost function below.
def cost(B):
    return rcost(B)

def rcost(B):
    return _rcost(B, [], 0)

def _rcost(B, A, s):
        if len(A) == len(B):
            # Base case
            cs = 0
            for i in range(1, len(A)):
                cs += abs(A[i] - A[i-1])
            return cs if cs > s else s
        else:
            ms = s
            for i in range(1, B[len(A)]+1):
                nA = []
                nA.extend(A)
                nA.append(i)
                cs = _rcost(B, nA, s)
                if cs > ms:
                    ms = cs
            return ms


data = [10, 1, 10, 1, 10]
print("Max diff frmo {} is {}\n".format(data, cost(data)))
                
