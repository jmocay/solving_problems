"""
Given a number represented by a list of digits,
find the next greater permutation of a number,
in terms of lexicographic ordering.

If there is not greater permutation possible,
return the permutation with the lowest value/ordering.

For example,
    The list [1,2,3] should return [1,3,2].
    The list [1,3,2] should return [2,1,3].
    The list [3,2,1] should return [1,2,3].
"""
def next_higher_permutation(arr):
    val = to_int(arr)
    perms = []
    generate(len(arr), arr, perms)
    perms.sort()
    i = binary_search(perms, val)
    if i == len(perms) - 1:
        return to_array(perms[0])
    else:
        return to_array(perms[i + 1])
    return perms

"""
    Generate all permutations for the numbers in the arr
    using Heap's algorithm.
"""
def generate(k, arr, perms):
    if k == 1:
        perms.append(to_int(arr))
    else:
        generate(k - 1, arr, perms)

        for i in range(k - 1):
            if k % 2 == 0:
                swap(arr, i, k - 1)
            else:
                swap(arr, 0, k - 1)
            generate(k - 1, arr, perms)

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def to_int(arr):
    return sum(arr[i] * pow(10, len(arr) - 1 - i) for i in range(len(arr)))

def to_array(val):
    return [int(c) for c in '{0}'.format(val)]

def binary_search(arr, val):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if val == arr[mid]:
            return mid
        elif val < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return None

if __name__ == '__main__':
    arr = [1,2,3]
    print(arr, 'next permutation: ', next_higher_permutation(arr))

    arr = [1,3,2]
    print(arr, 'next permutation: ', next_higher_permutation(arr))

    arr = [3,2,1]
    print(arr, 'next permutation: ', next_higher_permutation(arr))
