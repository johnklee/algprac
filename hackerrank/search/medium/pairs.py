#!/usr/bin/env python
import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr_set = list(set(arr))
    hit_num_set = set()

    for n in arr_set:
        if n <= k:
            continue

        if n not in hit_num_set and (n-k) in arr_set:
            hit_num_set.add(n)

    return len(hit_num_set)


print("{}".format(pairs(2, [1, 5, 3, 4, 2])))
print("{}".format(pairs(1, [1, 2, 3, 4])))

# Terminated due to timeout
