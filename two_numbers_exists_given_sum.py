"""
    Given a list of numbers and a number k,
    return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17,
    return true since 10 + 7 is 17.
"""
def two_number_exists_given_sum(arr, k):
    ndict = {}
    for i in arr:
        ndict[i] = None
    while len(ndict) > 0:
        i = ndict.popitem()
        if (k - i[0]) in ndict:
            return True
    return False

if __name__ == '__main__':
    arr = [10, 15, 3, 7]
    print(two_number_exists_given_sum(arr, 25))
    print(two_number_exists_given_sum(arr, 17))
    print(two_number_exists_given_sum(arr, 18))
    print(two_number_exists_given_sum(arr, 10))
    print(two_number_exists_given_sum(arr, 12))