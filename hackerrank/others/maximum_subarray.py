#!/usr/local/bin/python3
import sys
import unittest
r'''
https://www.youtube.com/watch?v=86CQq3pKSUw&index=63&list=WL&t=0s
'''

def maxsum_of_subary(an_ary):
    r'''
    Find the maximum sum of subarray in the given array {an_ary}

    @param an_ary(list):
        Target array to look for maximum sum of sub array
    '''
    return kadane(an_ary) 


def kadane(ary):
    cache_of_lms = [0] * len(ary)
    cache_of_lms[0] = ary[0]
    max_global = cache_of_lms[0]
    for i in range(1, len(ary)):
        cache_of_lms[i] = max(ary[i], ary[i] + cache_of_lms[i-1])
        if cache_of_lms[i] > max_global:
            max_global = cache_of_lms[i]

    return max_global


class FAT(unittest.TestCase):
    def test_01(self):
        for ary, a in [([-2, 3, 2, -1, 9], 13)]:            
            r = maxsum_of_subary(ary)
            print('a={}; r={}; ary={}'.format(a, r, ary))
            self.assertEqual(a, r, 'E={}; R={}: {}'.format(a, r, ','.join(list(map(lambda e:str(e), ary)))))


def main():
    tary = sys.argv[1:]
    maxsum = maxsum_of_subary(list(map(lambda e:int(e), tary)))
    print("Maximum sum of subarray from {{{}}} is {}!\n".format(','.join(tary), maxsum))

if __name__ == '__main__':
    main()
