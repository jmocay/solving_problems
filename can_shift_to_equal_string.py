"""
    Given two strings A and B,
    return whether or not A can be shifted some number of times to get B.

    For example, if A is abcde and B is cdeab, return true.
    If A is abc and B is acb, return false.
"""
def can_shift_to_equal_string(a, b):
    if len(a) != len(b):
        return False

    s = 0
    arr = [c for c in a]
    while s < len(b):
        tmp = ''.join(arr)
        if tmp == b:
            return True
        last = arr.pop()
        arr.insert(0, last)
        s += 1

    return False

if __name__ == '__main__':
    print(can_shift_to_equal_string('ab', 'abc'))
    print(can_shift_to_equal_string('abc', 'abc'))
    print(can_shift_to_equal_string('abcde', 'cdeab'))
    print(can_shift_to_equal_string('abc', 'acb'))