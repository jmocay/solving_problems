"""
    A number is considered perfect if its digits sum up to exactly 10.
    Given a positive integer n, return the n-th perfect number.
    For example, given 1, you should return 19. Given 2, you should return 28.
"""
def perfect_number(n):
    if n >= 1 and n < 10:
        return n * 10 + (10 - n)
    elif n > 10:
        s = "{0}".format(n)
        tot = 0
        for c in s:
            tot += int(c)
        if tot < 10:
            return n * 10 + (10 - tot)
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    n = 10
    for k in range(n + 1):
        print(perfect_number(k))
    print(perfect_number(105))
    