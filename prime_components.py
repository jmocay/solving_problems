"""
    Given an even number (greater than 2),
    return two prime numbers whose sum will be equal to the given number.

    A solution will always exist. See Goldbach’s conjecture.

    Example:

    Input: 4
    Output: 2 + 2 = 4
        If there are more than one solution possible, return the lexicographically smaller solution.

    If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

    [a, b] < [c, d]
    If a < c OR a==c AND b < d.
"""
def prime_components(n):
    primes = generate_primes(n)
    prime_dict = {}
    for prime in primes:
        prime_dict[prime] = None
    for prime in primes:
        if (n - prime) in prime_dict:
            return [prime, n - prime]
    return [] # no solution

"""
    Sieve of Eratosthenes algorithm
"""
def generate_primes(n):
    arr = (n+1)*[True]
    arr[0] = arr[1] = False
    p = 2
    while p <= n:
        for i in range(2*p, n+1, p):
            arr[i] = False
        i = p+1
        while i <= n and not arr[i]:
            i += 1
        if i > n:
            break
        p = i
    return [ el[0] for el in enumerate(arr) if el[1] ]

if __name__ == '__main__':
    for n in range(1, 51):
        print(2*n, prime_components(2*n))
