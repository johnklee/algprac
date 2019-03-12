#!/usr/local/bin/python3
r'''
https://www.youtube.com/watch?v=xOlhR_2QCXY&index=68&list=WL&t=0s
'''

kk_sol_mem = {}  # key as tuple(item index, rest weight); value as solution
def kk_sol(wlist, vlist, mw):
    r'''
    Solution to Knapsack problem

    @param wlist(list):
        List to hold weight of items
    @param vlist(list):
        List to hold value of items
    @param mw(int):
        Maximum weight the knapsack can stand

    @return
        List of item to hold with maximum value sum
    '''
    global kk_sol_mem
    kk_sol_mem.clear()
    return recv_kk_sol(0, mw, wlist, vlist, [])

def calc_values(slist, vlist):
    r'''
    Calculate the value sum of selsected item(s)

    @param slist(list):
        List of selection for each item
    @param vlist(list):
        List to hold value of items

    @return
        The sumed value of selected item(s)
    ''' 
    vsum = 0
    for i in range(len(slist)):
        if slist[i] > 0 :
            vsum += vlist[i]

    return vsum

def recv_kk_sol(rn, rw, wlist, vlist, slist):
    r'''
    @param rn(int):
        Current item index
    @param rw(int):
        Rest weight the knapsack can stand
    @param slist(list):
        Selection item list
    '''
    isol = kk_sol_mem.get((rn, rw), None)
     
    lb_sol = None
    if isol is not None:
        return isol
    elif rn >= len(wlist) or rw == 0:
        return slist
    elif wlist[rn] > rw:
        n_slist = slist[:]
        n_slist.append(0)
        lb_sol = recv_kk_sol(rn+1, rw, wlist, vlist, n_slist)
    else:
        n_slist = slist[:]
        n_slist.append(1)
        t1_sol = recv_kk_sol(rn+1, rw - wlist[rn], wlist, vlist, n_slist)
        n_slist = slist[:]
        n_slist.append(0)
        t2_sol = recv_kk_sol(rn+1, rw, wlist, vlist, n_slist)

        if calc_values(t1_sol, vlist) >= calc_values(t2_sol, vlist):            
            lb_sol = t1_sol
        else:
            lb_sol = t2_sol

    kk_sol_mem[(rn, rw)] = lb_sol
    return lb_sol   

import unittest


class FAT(unittest.TestCase):
    def test_d1(self):
        wlist = [1, 2, 4, 2, 5]
        vlist = [5, 3, 5, 3, 2]
        mw = 10

        slist = kk_sol(wlist, vlist, mw)
        elist = [1, 1, 1, 1, 0]
        print("Selection list={}".format(''.join(map(str, slist))))
        self.assertEqual(''.join(map(str, elist)), ''.join(map(str, slist)), "Something wrong")

    def test_d2(self):
        wlist = [1, 2, 4, 2, 5, 3,  2]
        vlist = [5, 3, 5, 3, 2, 10, 5]
        mw = 10

        slist = kk_sol(wlist, vlist, mw)
        elist = [1, 1, 0, 1, 0, 1, 1]
        print("Selection list={} with maximum value={:,d}".format(''.join(map(str, slist)), calc_values(slist, vlist)))
        self.assertEqual(''.join(map(str, elist)), ''.join(map(str, slist)), "Something wrong")
