#!/usr/bin/env python
r'''
https://www.hackerrank.com/challenges/journey-to-the-moon/problem
'''
import math
import os
import random
import re
import sys



class Node:
    def __init__(self, v):
        self.v = v
        self.neighbors = set()
        self.visit = False

    def addN(self, n):
        if n not in self.neighbors:
            self.neighbors.add(n)
            n.addN(self)

    def __hash__(self):
        return hash(self.v)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.v == other.v

    def n(self):
        for n in self.neighbors:
            yield n

    def dfs(self):
        from collections import deque
        root = self
        root.visit = True
        nlist = deque()
        nlist.append(root)
        vlist = []
        while len(nlist) > 0:
            node = nlist.popleft()
            vlist.append(node.v)
            for n in node.n():
                if not n.visit:
                    nlist.append(n)
                    n.visit = True

        return vlist
        

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    ndict = {}
    cty_list = []

    # Create graph
    for a, b in astronaut:
        if a not in ndict:
            ndict[a] = Node(a)
        if b not in ndict:
            ndict[b] = Node(b)

        ndict[a].addN(ndict[b])

    # Search disjoin set
    for node in ndict.values():
        if not node.visit:
            cty_list.append(node.dfs())
            print('Group-{}: {}'.format(node.v, cty_list[-1]))

    # Other distinct countury
    for i in range(n):
        if i not in ndict:
            cty_list.append(set([i])) 

    print('Total {} unique countries...{}'.format(len(cty_list), cty_list))

    # Calculate unique pairs
    if len(cty_list) == 1:
        return 0
    elif len(cty_list) == 2:
        return len(cty_list[0]) * len(cty_list[1])
    else:
        cty_len_list = map(len, cty_list)
        psum = cty_len_list[0] * cty_len_list[1]
        nsum = cty_len_list[0] + cty_len_list[1]
        for i in range(2, len(cty_len_list)):
            psum += nsum * cty_len_list[i]
            nsum += cty_len_list[i]

        return psum

#print("{}".format(journeyToMoon(5, [(0, 1), (2, 3), (0, 4)])))
#print("{}".format(journeyToMoon(4, [(0, 2)])))


import unittest

class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def test_01(self):
        tdatas = [
                    (5, [(0, 1), (2, 3), (0, 4)], 6),
                    (4, [(0, 2)], 5)
                 ]

        for n, astronaut, a in tdatas:
            r = journeyToMoon(n, astronaut)
            self.assertEqual(a, r, 'Expect={}; Real={}'.format(a, r))

    def test_02(self):
        tid = [1]
        tdatas = []
        for id in tid:
            with open('journey-to-the-moon.t{}'.format(id), 'r') as fh:
                na, pn = fh.readline().strip().split(' ')
                astronaut = []
                for i in range(int(pn)):
                    astronaut.append(map(int, fh.readline().split(' ')))
                with open('journey-to-the-moon.a{}'.format(id), 'r') as fh2:
                    tdatas.append((int(na), astronaut, int(fh2.readline())))

        for n, astronaut, a in tdatas:
            r = journeyToMoon(n, astronaut)
            self.assertEqual(a, r, 'Expect={}; Real={}\n{}'.format(a, r, astronaut))
