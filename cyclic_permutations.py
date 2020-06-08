"""
    Given the number represented by the digits
        a0,a1,...,an-1 = a0a1a2...an-1
    Generate the permutations:
        a0,a1,...,an-1 = a0a1a2...an-1
        a1,a2,...,a0
        ...
        an-1,a0,...,an-2
"""
def cycling_permutations(n):
    cnt = digit_count(n)

    perm =  n
    perms = [perm]
    while True:
        rem = perm % 10
        div = perm // 10
        perm = (rem % 10) * 10 ** (cnt - 1) + div
        if perm == n:
            break
        perms.append(perm)

    return perms

def digit_count(n):
    digit_cnt = 0
    while n > 0:
        digit_cnt += 1
        n = n // 10
    return digit_cnt

if __name__ == '__main__':
    data = [
        1,
        12,
        123,
        1234,
    ]
    for n in data:
        print(n, digit_count(n))

    n = 7923
    print(cycling_permutations(n))
