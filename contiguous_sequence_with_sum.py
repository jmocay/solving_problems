"""
    Given a list of integers and a number n,
    return which contiguous elements of the list sum to n.

    For example:
        If the list is [1, 2, 3, 4, 5] and n is 9,
        then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""
def contiguous_sequence_with_sum(arr, n):
    start = 0
    end = 0
    total = 0
    while start < len(arr):
        i = end
        while i < len(arr) and total < n:
            total += arr[i]
            i += 1
        end = i + 1 if i == end else i
        if total == n:
            return arr[start:end-start]
        elif total > n:
            total -= arr[start]
        start += 1
    return []

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = 12
    for k in range(1, n+1):
        print("sum: {0}, sequence: {1}".format(k, contiguous_sequence_with_sum(arr, k)))