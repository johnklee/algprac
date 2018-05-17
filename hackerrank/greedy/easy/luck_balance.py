#!/usr/bin/env python
import math
import os
import random
import re
import sys

r'''
https://www.hackerrank.com/challenges/luck-balance/problem
'''

# Complete the luckBalance function below.
def luckBalance(n, k, contests):
    luck_sum = 0
    important_game_luck_list = []
    for l, t in contests:
        if t == 0:
            luck_sum += l
        else:
            important_game_luck_list.append(l)

    # Sorting in descending order
    important_game_luck_list = sorted(important_game_luck_list, reverse=True)

    # Add up all luck in losing game
    for i in range(min(k, len(important_game_luck_list))):
        luck_sum += important_game_luck_list[i]

    # Minus back all luck in winning game
    if k < len(important_game_luck_list):
        for i in important_game_luck_list[k:]:
            luck_sum -= i

    return luck_sum

import unittest 


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        self.assertEqual(luckBalance(3, 2, [(5, 1), (1, 1), (4, 0)]), 10)
        self.assertEqual(luckBalance(3, 1, [(5, 1), (1, 1), (4, 0)]), 8)

    def test_02(self):
        real = luckBalance(6, 3, [(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)])
        self.assertEqual(real, 29, 'Expect:29; Real:{}'.format(real))
