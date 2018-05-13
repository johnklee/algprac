#!/usr/bin/env python
from pprint import pprint
r'''
https://www.hackerrank.com/challenges/magic-square-forming/problem
'''

def isMagic(s, c, r):
    r'''
    Check if the given column and row all sum to magic number 15
    '''
    if (s[0][c] + s[1][c] + s[2][c]) != 15:
        return False
    if (s[r][0] + s[r][1] + s[r][2]) != 15:
        return False
    return True


def isUnique(s, c, r):
    r'''
    Confirm the element at given row and column to be unique.
    '''
    eset = set()
    for i in range(3):
        eset.add(s[r][i])
        eset.add(s[i][c])

    return len(eset) == 5


def l2s(alist):
    r'''
    Translate list into square
    '''
    s = []
    ''' square '''
    r = []
    ''' row list '''
    i = 0
    ''' position of element '''

    for e in alist:
        r.append(e)    
        i += 1
        if i == 3:
            s.append(r)
            r = []
            i = 0
 
    return s

def isMagicSquare(s):
    r''' Check the given square to be magic or not'''
    for i in range(3):
        if not isMagic(s, i, i):
            return False
    return True


def subRlist(rlist):
    r''' Pick up each element from give list and return (Picked element, the list with others element '''
    if len(rlist) == 1:
        yield (rlist[0], [])
    else:
        for i in range(len(rlist)):
            olist = []
            olist.extend(rlist[0:i])
            olist.extend(rlist[i+1:len(rlist)])
            yield(rlist[i], olist)

def _msGen(clist, rlist):
    if len(rlist) == 0:
        yield clist
    else:    
        for e, slist in subRlist(rlist):
            olist = []
            olist.extend(clist)
            olist.append(e)
            for s in _msGen(olist, slist):
                yield s 

def msGen():
    r''' Matic Square Generator '''
    for l in _msGen([], [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        s = l2s(l)
        if isMagicSquare(s):
            print("\"{}\\n\" +".format(str(l)[1:-1]))
            yield s 


ts = l2s(list(range(1, 10)))
pprint(l2s(list(range(1, 10)))) 
print("ts is magic at (2,2)? {}".format(isMagic(ts, 2, 2)))
print("ts is unique at (2,2)? {}".format(isUnique(ts, 2, 2)))

# Testing API:subRlist
#for e, slist in subRlist([1, 2, 3]):
#    print('{}\t{}'.format(e, slist))

# 1) Collect all magic square
all_magic_squares = []
c = 0
for ms in msGen():
    all_magic_squares.append(ms)
    #pprint(ms)
    c += 1

print('\nTotal {} magic square(s) being collected!'.format(c))


def costInTrans(ts, ms):
    r''' Calculate the cost in the transformation'''
    cost = 0
    for r in range(3):
        for c in range(3):
            cost += abs(ts[r][c] - ms[r][c])

    return cost

# 2) Select magic square with minimum cost in transformation
def selectMS(ts):
    r''' Select Magic Square with minimum transformation costi

    @param ts(list)
        Target Square

    @return
        Tuple(Magic Square, Cost)'''
    mms = None
    ''' Magic Square with Minimum Transformation Cost'''
    cs = None
    ''' Current Cost '''
    for ms in all_magic_squares:
        cost = costInTrans(ts, ms)
        if cs is None or cost < cs:
            mms = ms
            cs = cost
        if cost == 0:
            break

    return (mms, cs)


# 3) Test Case(s)
import unittest
class FATestCase(unittest.TestCase):
    def testFAT(self):
        ts = [[4,8,2], [4,5,7], [6,1,6]]
        ''' Target Square '''

        mms, cs = selectMS(ts)
        print('Target Square={} with minimum cost={} from Magic Square={}'.format(ts, cs, mms))
        self.assertEqual(4, cs, 'Expected result is 4 while given {}'.format(cs))
    
