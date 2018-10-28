#!/usr/local/bin/python3
r'''
Array Manipulation in Place: Coding Interview Question in Whiteboard Thursday
'''
def move_zero_to_end(alist):
    nz_list = []

    for i in range(len(alist)):
        if alist[i] != 0:
            nz_list.append(i)

    if len(nz_list) == len(alist) or len(nz_list) == 0:
        return alist
    else:
        for i in range(len(nz_list)):
            alist[i] = alist[nz_list[i]]

        for i in range(len(nz_list), len(alist)):
            alist[i] = 0

    return alist

print(move_zero_to_end([0, 1, 2, 0, 3, 0, 4]))


import unittest


class FAT(unittest.TestCase):
    def test_d1(self):
        alist = [0, 1, 2, 0, 3, 0, 4]
        blist = move_zero_to_end(alist[:])
        self.assertEqual('1,2,3,4,0,0,0', ','.join(map(str, blist)))
