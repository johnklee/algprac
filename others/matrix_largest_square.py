#!/usr/local/bin/python3
r'''
https://www.youtube.com/watch?v=FO7VXDfS8Gk&index=73&list=WL&t=0s
'''
import math


mem_dict = {}
def get_largest_square(mtx):
    r'''
    Get the largest square from the given matrix.
    e.g.
    [
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1]
    ]
    The largest square of this matrix is 3

    @param mtx(list):
        A two dimension array.
    '''
    global mem_dict
    mem_dict.clear()

    max_ss = 0
    for ri in range(len(mtx)):
        for ci in range(len(mtx[ri])):
            if mtx[ri][ci] > 0:
                rv = recv_ls(ri, ci, mtx)
                if rv > max_ss:
                    max_ss = rv
                #print("[{},{}]->{}".format(ri, ci, rv))

    return max_ss


def recv_ls(ri, ci, mtx):
    r'''
    Get the largest square in position (ri, ci) from the Matrix as <mtx>
    '''
    if ri >= len(mtx) or ci >= len(mtx[ri]):
        return 0
    elif mtx[ri][ci] == 0:
        return 0
    else:
        if (ri, ci) in mem_dict:
            return mem_dict[(ri, ci)]
        else:
            val = 1 + min([recv_ls(ri, ci+1, mtx), recv_ls(ri+1, ci+1, mtx), recv_ls(ri+1, ci, mtx)])
            mem_dict[(ri, ci)] = val
            #print("\t[{},{}]->{}".format(ri, ci, val))
            return val


import unittest

class UAT(unittest.TestCase):
    def test_s1(self):
        test_mtx = [
            [1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1]
        ]
        exp = 3
        rel = get_largest_square(test_mtx)
        self.assertEqual(exp, rel, 'E={};R={}'.format(exp, rel))
