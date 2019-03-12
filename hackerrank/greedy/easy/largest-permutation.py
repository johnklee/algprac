#!/usr/bin/env python3

# Complete the largestPermutation function below.
def largestPermutation_v1(k, arr):
    sc = k  # Swap count
    pi = len(arr)
    ci = 0
    while sc > 0 and pi > 0:
        #print("{}: ci={}; pi={}".format(arr, ci, pi))
        sp = arr[ci:].index(pi)
        #print("\tsp={}".format(sp))
        if sp != 0:
            sc -= 1
            arr[ci], arr[ci+sp] = arr[ci+sp], arr[ci]

        ci += 1
        pi -= 1
        
    return arr

def largestPermutation(k, arr):
    arr_dict = {}
    for i in range(len(arr)):
        arr_dict[arr[i]] = i

    sc = k
    pi = len(arr)
    ci = 0
    while sc > 0 and pi > 0:
        sp = arr_dict[pi]
        if sp != ci:
            sc -= 1
            arr[ci], arr[sp] = arr[sp], arr[ci]
            arr_dict[arr[sp]] = sp

        ci += 1
        pi -= 1

    return arr

print("{}".format(' '.join(map(str, largestPermutation(2, [1, 2, 3, 4])))))
