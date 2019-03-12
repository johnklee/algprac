#!/usr/local/bin/python3
r'''
https://www.hackerrank.com/challenges/kruskalmstrsub/problem

@see
    - http://localhost/jforum/posts/list/914.page (Prim)
    - http://localhost/jforum/posts/list/915.page (Kruskal)
'''

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    cns_dict = {}
    ''' connected node dict '''
    sum_weight = 0
    ''' The total wegith of Really Special SubTree '''

    for i in range(1, g_nodes+1):
        cns_dict[i] = set([i])    

    ftw_list = []
    for f, t, w in zip(g_from, g_to, g_weight):
        ftw_list.append((f, t, w))

    print("")
    for f, t, w in sorted(ftw_list, key=lambda t:t[2]):
        fs = cns_dict[f]
        ts = cns_dict[t]
        if t in fs and f in ts:
            # Form a loop
            continue

        us = fs | ts
        for n in us:
            cns_dict[n] = us

        sum_weight += w
        print("Select {}->{} with weight={} ({})".format(f, t, w, us))
        if len(us) == g_nodes:
            break

    return sum_weight
     

import unittest


class FAT(unittest.TestCase):
    def read_tc(self, tn):
        if __file__.startswith('./'):
            sp = __file__[:2]
        else:
            sp = __file__

        tf = '{}.t{}'.format(sp.split('.')[0], tn)
        with open(tf, 'r') as fh:
            g_nodes, g_edges = map(int, fh.readline().rstrip().split())

            g_from = [0] * g_edges
            g_to = [0] * g_edges
            g_weight = [0] * g_edges

            for i in range(g_edges):
                g_from[i], g_to[i], g_weight[i] = map(int, fh.readline().rstrip().split())

            exp = int(fh.readline())

        return (g_nodes, g_from, g_to, g_weight, exp)

    def test_d1(self):
        exp = 12
        g_nodes = 4
        g_from =    [1, 1, 4, 2, 3, 3]
        g_to =      [2, 3, 1, 4, 2, 4]
        g_weight =  [5, 3, 6, 7, 4, 5]
        rel = kruskals(g_nodes, g_from, g_to, g_weight)
        self.assertEqual(exp, rel, 'E={};R={}'.format(exp, rel))

    def test_t2(self):
        g_nodes, g_from, g_to, g_weight, exp = self.read_tc(2)
        rel = kruskals(g_nodes, g_from, g_to, g_weight)
        self.assertEqual(exp, rel, 'E={};R={}'.format(exp, rel))
