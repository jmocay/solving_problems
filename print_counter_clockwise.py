"""
    Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

    For example, given the following matrix:

    [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]]
    You should print out the following:

    1
    2
    3
    4
    5
    10
    15
    20
    19
    18
    17
    16
    11
    6
    7
    8
    9
    14
    13
    12
"""
def print_counter_clockwise(arr):
    rows = len(arr)
    if rows == 0:
        return
    cols = len(arr[0])
    if cols == 0:
        return

    n = rows * cols

    left = 0
    right = len(arr[0]) - 1
    top = 0
    bottom = len(arr) - 1

    d = 1
    i = 0
    j = 0
    k = 0
    while k < n:
        if d == 1: # right
            j0 = j
            while j <= right:
                print(arr[i][j])
                k += 1
                j += 1
            j = j if j == j0 else (j - 1)
            top += 1
            if i <= bottom:
                i += 1
            d = 2
        elif d == 2: # down
            i0 = i
            while i <= bottom:
                print(arr[i][j])
                k += 1
                i += 1
            i = i if i == i0 else (i - 1)
            right -= 1
            if j >= left:
                j -= 1
            d = 3
        elif d == 3: # left
            j0 = j
            while j >= left:
                print(arr[i][j])
                k += 1
                j -= 1
            j = j if j == j0 else (j + 1)
            bottom -= 1
            if i >= top:
                i -= 1
            d = 4
        elif d == 4: # up
            i0 = i
            while i >= top:
                print(arr[i][j])
                k += 1
                i -= 1
            i = i if i == i0 else (i + 1)
            left += 1
            if j <= right:
                j += 1
            d = 1

if __name__ == '__main__':
    arr = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
    print_counter_clockwise(arr)