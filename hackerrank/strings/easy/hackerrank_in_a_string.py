#!/usr/bin/env python
import unittest
r'''
https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
'''
magic_str = 'hackerrank'

def _recvHackerrankInString(s, c, p):
    r'''
    @param s(str):
        String to look for 'hackerrank'

    @param c(int):
        Start position of given <s>
    
    @param p(int):
        The evaluation point from 'hackerrank'
    '''
    if p >= len(magic_str):
        return True
    else:
        for i in range(c, len(s)):
            if s[c] == magic_str[p] and _recvHackerrankInString(s, i+1, p+1):
                return True
                
        return False


def hackerrankInString(s):
    r'''
    Check the 'hackerrank' in given string <s>
    '''
    if _recvHackerrankInString(s, 0, 0):
        return 'YES'
    else:
        return 'NO'


class FAT(unittest.TestCase):
    def setUp(self):
        self.datas = {
                      "hereiamstackerrank":"YES",
                      "hackerworld":"NO",
                      "haacckkerrannkk":"YES",
                      "haacckkerannk":"NO"
                     }
        ''' testing data: key=testing string; value=expected result'''

    def test_fat(self):
        for tstr, expr in self.datas.items():
            real = hackerrankInString(tstr)
            print('{}: Real={}; Expr={}'.format(tstr, real, expr))
            self.assertEqual(real, expr, 'Fail in data=\'{}\''.format(tstr))
