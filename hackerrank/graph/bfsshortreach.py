#!/usr/bin/env python
import math
import os
import random
import re
import sys
import logging
from collections import deque
from Queue import Queue

r'''
https://www.hackerrank.com/challenges/bfsshortreach/problem
'''
LOGGER_LEVEL = logging.DEBUG # Debug:10, Info:20, Warning:30
#FORMATTER = logging.Formatter('%(message)s')
logger = logging.getLogger(__file__)
console = logging.StreamHandler()
console.setLevel(LOGGER_LEVEL)
#console.setFormatter(FORMATTER)
logger.setLevel(LOGGER_LEVEL)
logger.addHandler(console)

class Node:
    def __init__(self, val):
        self.v = val
        self.neighbors = []
        self.d = -1  # Distance
        self.visit = False

    def addN(self, n):
        r'''
        Add node as neighbor
        '''
        self.neighbors.append(n)

    def nGen(self):
        for n in self.neighbors:
            yield n


# Complete the bfs function below.
def bfs(n, m, edges, s):
    r'''
    @param n(int):
        Number of node
    @param m(int):
        Number of edge
    @param edges(list):
        List of tuple(node1, node2)
    @param s(int):
        Start point
    '''
    nMap = {}   # Node namp
    dMap = {}   # Distance map

    for i in range(1, n+1):
        nMap[i] = Node(i)

    edgeSet = set()
    for n1, n2 in edges:
        if (n1, n2) in edgeSet or (n2, n1) in edgeSet:
            continue
        nMap[n1].addN(nMap[n2])
        nMap[n2].addN(nMap[n1])
        edgeSet.add((n1, n2))
        edgeSet.add((n2, n1))

    root = nMap[s]
    root.d = 0
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        if not node.visit:
            for snode in node.nGen():
                if not snode.visit:                    
                    if snode.d == -1:
                        snode.d = node.d + 1
                    q.append(snode)
                    
        node.visit = True

    dlist = []
    nlist = list(range(1, n+1))
    nlist.remove(s)
    for ni in nlist:
        node = nMap[ni]
        d = node.d * 6 if node.d > 0 else -1
        dlist.append(d)

    return tuple(dlist)
 

import unittest


class FATestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def readData(self, fp):
        qlist = []
        with open(fp, 'r') as fh:
            qnum = int(fh.readline().strip())
            for i in range(qnum):
                n, e = map(int, fh.readline().split())  # number of node, number of edge
                edges = []
                for j in range(e):
                    edges.append(map(int, fh.readline().split()))
                s = int(fh.readline().strip())
                qlist.append((n, e, edges, s))
        return qlist

    def readExp(self, fp):
        elist = []
        with open(fp, 'r') as fh:
            for line in fh:
                elist.append(map(int, line.split()))
        return elist

    def test01(self):
        self.assertEqual(bfs(4, 2, [[1,2],[1,3]], 1), (6,6,-1))

    def test02(self):
        self.assertEqual(bfs(3,1, [[2,3]], 2), (-1, 6))

    def test03(self):
        self.assertEquals(bfs(4, 3, [[1,2], [2,3], [3,4]], 1), (6, 12, 18))

    def test04(self):
        qlist = self.readData('bfsshortreach_t1.data')
        elist = self.readExp('bfsshortreach_t1.exp')
        for i in range(len(qlist)):
            q = qlist[i]
            e = elist[i]
            r = bfs(q[0], q[1], q[2], q[3])
            self.assertEquals(r, tuple(e), 'Real={}\nExp={}\n'.format(r, e))
