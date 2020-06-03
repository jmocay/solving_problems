"""
    Given an integer n and a list of integers l,
    write a function that randomly generates a number from 0 to n-1
    that isn't in l (uniform).
"""
from datetime import datetime
from random import randint

def randint_exclude_list(n, l):
    excluded = {}
    for k in l:
        excluded[k] = None
    arr = []
    for i in range(n):
        if i in excluded:
            continue
        arr.append(i)
    return arr[randint(0, len(arr)-1)]

if __name__ == '__main__':
    l = [4, 6]
    n = 10
    for i in range(10):
        print(randint_exclude_list(n, l))