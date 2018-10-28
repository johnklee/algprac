#!/usr/local/bin/python3
r'''
https://www.hackerrank.com/challenges/jeanies-route/problem
'''
import os
import sys

#
# Complete the jeanisRoute function below.
#
def jeanisRoute(n, clist, roads):
    r'''
    @param n(list):
        Number of city
    @param clist(list):
        List of city need to visit
    @param roads(list):
        List of roads to connect each city
    '''
    qdict = {} # Quick path: with key as tuple(src, dest); 
               # value as cost traveling from source city to
               # destination city
    cdict = {} # Connecting dict

    for s, d, w in roads:
        qdict[(s, d)] = w
        qdict[(d, s)] = w
        if s in cdict:
            cdict[s].append(d)
        else:
            cdict[s] = [d]

        if d in cdict:
            cdict[d].append(s)
        else:
            cdict[d] = [s]

    # Fill-up qdict
    for i in range(1, n+1):
        if i not in clist:
            continue

        for j in range(i+1, n+1):
            if (i, j) not in qdict:
                gcs = sys.maxsize
                gnc = None
                for nc in cdict[i]:
                    if (nc, j) in qdict:
                        cs = qdict[(nc, j)]
                        #break
                    else:
                        cs = lookUp(i, nc, j, cdict, qdict)

                    #print('\tGot {}->{}={} (from={})'.format(nc, j, cs, i))
                    if cs < gcs:
                        gcs = cs
                        gnc = nc

                gcs += qdict[(i, gnc)]
                qdict[(i, j)] = gcs
                qdict[(j, i)] = gcs
                #print('Got {}->{}={}!'.format(i, j, gcs))

    # Look up best search path
    min_d = sys.maxsize
    for nc in clist:
        tmp_clist = clist[:] 
        tmp_clist.remove(nc)
        d = visit_cts(nc, tmp_clist, qdict)
        if d < min_d:
            min_d = d
            print("Got minimum distance={} starting from {}!".format(min_d, nc)) 

    return min_d
               
def lookUp(frm, src, dst, cdict, qdict):
    gcs = sys.maxsize
    gnc = None
    for nc in cdict[src]:
        if nc == frm:
            continue

        if nc == dst:
            return qdict[(src, nc)] 
        elif (nc, dst) in qdict:
            return qdict[(src, nc)] + qdict[(nc, dst)]
        else:
            cs = lookUp(src, nc, dst, cdict, qdict)
            if cs < gcs:
                gcs = cs
                gnc = nc

    if gcs != sys.maxsize:
        gcs += qdict[(src, nc)]
        qdict[(src, dst)] = gcs
        qdict[(dst, src)] = gcs
        gcs += qdict[(src, nc)]
        return gcs
    else:
        return gcs
        

def visit_cts(sc, clist, qdict):
    r'''
    Visit all cities in <clist> with starting city as <sc>
    '''
    if len(clist) == 1:
        return qdict[(sc, clist[0])]
    else:
        min_d = sys.maxsize
        min_nc = None
        for nc in clist:
            tmp_clist = clist[:]
            tmp_clist.remove(nc)
            d = visit_cts(nc, tmp_clist, qdict)
            if d < min_d:
                min_d = d
                min_nc = nc
        
        return qdict[(sc, min_nc)] + min_d

n = 5
clist = [1, 3, 4]
roads = [
            (1, 2, 1),
            (2, 3, 2),
            (2, 4, 2),
            (3, 5, 3)
        ]     
''' testing data '''

def read_tc(tn):
    if __file__.startswith('./'):
        script_name = __file__[2:]
    else:
        script_name = __file__
    tc_fname = "{}.t{}".format(script_name.split('.')[0], tn)

    with open(tc_fname) as fh:
        n, k = fh.readline().split()
        n = int(n)
        k = int(k)
        clist = list(map(int, fh.readline().strip().split()))
        roads = []
        for i in range(n-1):
            roads.append(list(map(int, fh.readline().rstrip().split())))

        return (n, clist, roads)

min_d = jeanisRoute(n, clist, roads) 
from pprint import pprint
pprint(min_d)
