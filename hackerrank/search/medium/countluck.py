#!/usr/local/bin/python3
r'''
https://www.hackerrank.com/challenges/count-luck/problem
'''

# Complete the countLuck function below.
def countLuck(matrix, k):
    mtx = Mtx(matrix)
    if mtx.go() == k:
        return 'Impressed'
    else:
        return 'Oops!'


class Mtx:
    def __init__(self, matrix):
        self.maze_dat=[]

        self.start = None
        self.end = None
        ri = 0
        for line in matrix:
            row_dat = []
            ci = 0
            for c in line.strip():
                if c == '.':
                    row_dat.append(0)
                elif c == 'X':
                    row_dat.append(-1)
                elif c == 'M':
                    row_dat.append(0)
                    self.start = (ri, ci)
                elif c == '*':
                    row_dat.append(2)
                    self.end = (ri, ci)
                ci += 1
            ri += 1
            self.maze_dat.append(row_dat)

        self.maze_size = (len(self.maze_dat), len(self.maze_dat[0]))

    def next_step(self, loc):
        ri = loc[0]
        ci = loc[1]
        nsteps = []
        if ri > 0 and self.maze_dat[ri-1][ci] in [0, 2]:
            nsteps.append((ri-1, ci))

        if ri+1 < self.maze_size[0] and self.maze_dat[ri+1][ci] in [0, 2]:
            nsteps.append((ri+1, ci))

        if ci > 0 and self.maze_dat[ri][ci-1] in [0, 2]:
            nsteps.append((ri, ci-1))

        if ci+1 < self.maze_size[1] and self.maze_dat[ri][ci+1] in [0, 2]:
            nsteps.append((ri, ci+1))

        return nsteps

    def is_done(self, loc):        
        return loc[0] == self.end[0] and loc[1] == self.end[1]

    def is_junct(self, loc):
        ri = loc[0]
        ci = loc[1]
        wg = 0
        dr = 0
        ''' way to go '''
        if ri > 0:
            dr += 1
            if self.maze_dat[ri-1][ci] in [0, 2]:
                wg += 1

        if ri+1 < self.maze_size[0]:
            dr += 1
            if self.maze_dat[ri+1][ci] in [0, 2]:
                wg += 1

        if ci > 0:
            dr += 1
            if self.maze_dat[ri][ci-1] in [0, 2]:
                wg += 1

        if ci+1 < self.maze_size[1]:
            dr += 1
            if self.maze_dat[ri][ci+1] in [0, 2]:
                wg += 1

        #print("{} with dr={}; wg={}".format(loc, dr, wg))
        return wg > 1

    def walk(self, loc):
        #print("Walk on {}".format(loc))
        self.maze_dat[loc[0]][loc[1]] = 1

    def __str__(self):
        maze_str = ''
        for row in self.maze_dat:
            maze_str += "{}\n".format(''.join(map(lambda e:"{:>2}".format(str(e)), row)))

        return maze_str

    def __repr__(self):
        return self.__str__()

    def go(self):
        loc = list(self.start)
        dst = list(self.end)

        #print("start={}; end={}".format(loc, dst))
        self.jp_list = []
        if self.is_junct(loc):
            self.jp_list.append(loc)

        self.walk(loc)
        while not self.is_done(loc):
            is_back = False
            next_steps = self.next_step(loc)
            if len(next_steps) == 0:
                # Back to previous juncture point
                next_steps = self.next_step(self.jp_list[-1])
                while len(next_steps) == 0:
                    #print("Back to juncture point={}".format(self.jp_list[-1]))
                    self.jp_list = self.jp_list[:-1] 
                    next_steps = self.next_step(self.jp_list[-1])
                    is_back = True

            loc = next_steps[0]
            if self.is_done(loc):
                break

            if not is_back and self.is_junct(loc):
                self.jp_list.append(loc)
                #print("** New juncture point={} **".format(loc))

            self.walk(loc)              
        #print("Done!")
        return len(self.jp_list)

import unittest

def read_tc(tn):
    if __file__ .startswith('./'):
        sfn = __file__[2:]
    else:
        sfn = __file__

    tc_file = '{}.t{}'.format(sfn.split('.')[0], tn)
    tc_list = []
    with open(tc_file, 'r') as fh:
        tc_num = int(fh.readline())
        for i in range(tc_num):
            row_num = int(fh.readline().split(' ')[0])
            maze = []
            for ri in range(row_num):
                maze.append(fh.readline().strip())

            k, exp = fh.readline().split()
            tc_list.append((maze, int(k), exp.strip()))

    return tc_list


class FAT(unittest.TestCase):
    def test_d1(self):
        test_dat = [
                    (['*.M', '.X.'], 1, 'Impressed'),
                    (['.X.X......X', '.X*.X.XXX.X', '.XX.X.XM...', '......XXXX.'], 3, 'Impressed'),
                    (['.X.X......X', '.X*.X.XXX.X', '.XX.X.XM...', '......XXXX.'], 4, 'Oops!')
                   ]
        for ms, k, e in test_dat:
            r = countLuck(ms, k)
            self.assertEqual(e, r, 'E={}; R={}'.format(e, r))


    def test_rd(self):
        for tn in [2, 3]:
            sn = 0
            print("TN={}".format(tn))
            for maze, k, e in read_tc(tn):
                r = countLuck(maze, k)
                self.assertEqual(e, r, 'E={}; R={} in TC={}-{}'.format(e, r, tn, sn))
                sn += 1

mx = Mtx(['XXXXXXXXXXXXXXXXX', 'XXX.XX.XXXXXXXXXX', 'XX.*..M.XXXXXXXXX', 'XXX.XX.XXXXXXXXXX', 'XXXXXXXXXXXXXXXXX'])
