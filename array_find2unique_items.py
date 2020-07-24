"""
    Given an array of integers in which two elements appear exactly once
    and all other elements appear exactly twice,
    find the two elements that appear only once.

    For example, given the array [2, 4, 6, 8, 10, 2, 6, 10],
    return 4 and 8. The order does not matter.
"""

"""
    Solution 1 using a dictionary.
    This runs in linear time but takes O(n) space
"""
def find2unique(arr):
    unqs = {}
    for k in arr:
        if k in unqs:
            del unqs[k]
        else:
            unqs[k] = None
    return [k for k in unqs.keys()]

"""
    Solution 2
    Follow-up: Can you do this in linear time and constant space?
"""

if __name__ == '__main__':
    print(find2unique([2, 4, 6, 8, 10, 2, 6, 10]))