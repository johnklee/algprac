#!/usr/local/bin/python3
r'''
https://www.youtube.com/watch?v=VeJOswJTDos&index=75&list=WL&t=24s

[2,1,6,9,4,3] => [1,2,3,4]
'''
def longest_conseq(alist):   
    cache_rst = {}
    max_clen = -1
    max_cary = None
    for e in alist:
        if e in cache_rst:
            continue
        else:
            # Look for the head
            head = e
            pt = head - 1
            while pt in alist:
                head = pt
                pt = pt - 1

            # Look for the tail
            tail = e
            pt = tail + 1
            while pt in alist:
                tail = pt
                pt = pt + 1

            seq_len = tail - head + 1
            seq_ary = []
            for i in range(head, tail+1):
                cache_rst[i] = seq_len
                seq_ary.append(i)

            if seq_len > max_clen:
                max_clen = seq_len
                max_cary = seq_ary

    return max_cary


import unittest


class FAT(unittest.TestCase):
    def test_01(self):
        test_ary = [2,5,7,1,3,10,4,9]
        exp_ary = [1, 2, 3, 4, 5]
        rel_ary = longest_conseq(test_ary)
        self.assertEqual(exp_ary, rel_ary, 'E:{}; R:{}'.format(exp_ary, rel_ary))




