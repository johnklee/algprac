#!/usr/bin/env python3
r'''
https://www.hackerrank.com/challenges/a-chessboard-game-1/problem
'''
import math
import os
import random
import re
import sys


current_row = None
current_col = None
hist_moves = {}

# Known truth
#          x  y
hist_moves[(1, 1)] = False
hist_moves[(2, 1)] = False
hist_moves[(3, 1)] = True
hist_moves[(1, 2)] = False
hist_moves[(2, 2)] = False
hist_moves[(3, 2)] = True
hist_moves[(1, 3)] = True
hist_moves[(2, 3)] = True
hist_moves[(3, 3)] = True

def print_hm(r, c):
    global hist_moves
    n = min(max(r, c) + 1, 15)
    for i in range(1, n):
        rows = list(filter(lambda t: t[0][0] == i, hist_moves.items()))
        rdict = {}
        for r in rows:
            rdict[r[0][1]] = r[1]

        for i in range(1, n):
            if i in rdict:
                print("{}\t".format(rdict[i]), end='')
            else:
                print("None\t", end='')

        print("")

    print("")

def build_hm():
    global hist_moves
    global current_row
    global current_col
    for i in range(1, 16):
        for j in range(1, 16):
            val = hist_moves.get((i, j), None)
            if val is None:
                is_done = False
                is_miss = False
                for _r, _c in next_moves(i, j):
                    val = hist_moves.get((_r, _c), None)
                    if val is None:
                        is_miss = True
                        break
                    elif not val:
                        hist_moves[(i, j)] = True
                        is_done = True
                        break

                if not is_done and not is_miss:
                    hist_moves[(i, j)] = False
                    reverse_move(i, j)
                    #print_hm(i+1, j+1) 
                    
            elif not val:
                reverse_move(i, j)
                #print_hm(i+1, j+1)

            if i == current_row and j == current_col:
                break
                

# Complete the chessboardGame function below.
def chessboardGame(r, c):
    global hist_moves
    global current_row
    global current_col

    current_row = r
    current_col = c
    # Build up history moves
    if (r, c) not in hist_moves:
        build_hm()

    # Return result
    #print("")
    #print_hm(r, c)
    return 'First' if hist_moves[(r, c)] else 'Second'

def reverse_move(c, r):
    global hist_moves
    tc = c + 2
    tr = r + 1
    if tc <= 15 and tr <= 15:
        hist_moves[(tc, tr)] = True
    
    tc = c + 2
    tr = r - 1
    if tc <=15 and tr >= 1:
        hist_moves[(tc, tr)] = True

    tr = r + 2
    tc = c + 1
    if tc <= 15 and tr <= 15:
        hist_moves[(tc, tr)] = True

    tr = r + 2
    tc = c - 1
    if tr <= 15 and tc >= 1:
        hist_moves[(tc, tr)] = True

def next_moves(x, y):
    moves = []
    if x - 2 > 0:
        moves.append((x - 2, y + 1))
        if y > 1:
            moves.append((x - 2, y - 1))

    if y - 2 > 0:
        moves.append((x + 1, y - 2))
        if x > 1:
            moves.append((x - 1, y - 2))

    return moves

def has_next_move(x, y):
    if x - 2 > 0:
        return True
    if y - 2 > 0:
        return True

    return False

r = 8
c = 8
print("=== ({}, {})->{} ===".format(r, c, chessboardGame(r, c)))


import unittest


class FAT(unittest.TestCase):
    def setUp(self):
        pass

    def read_tc(self, tn):
        module_name = __file__.split('.')[0]
        test_case_fname = "{}.t{}".format(module_name, tn)
        answer_fname = "{}.a{}".format(module_name, tn)
        cordi_list = []
        answers = []
        with open(test_case_fname, 'r') as fh:
            fh.readline() # tcn
            for line in fh:
                cordi_list.append(tuple(map(int, line.split())))

        print('Total {:,d} cordi'.format(len(cordi_list)))

        with open(answer_fname, 'r') as fh:
            for line in fh:
                answers.append(line.strip())

        print("Total {:,d} answer".format(len(answers)))

        return (cordi_list, answers)

    def test_01(self):
        pi = 0
        cordi_list, answers = self.read_tc(1)
        for i in range(len(cordi_list)):
            pi += 1
            pos = cordi_list[i]
            asw = answers[i]
            rel = chessboardGame(*pos)
            self.assertEqual(asw, rel, 'Exp={}; Rel={} on pos={} from pi={}'.format(asw, rel, pos, pi))
            
