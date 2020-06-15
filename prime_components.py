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
    arr = [k for k in range(2, n+1)]

    i = 0 # prime index
    p = arr[i]
    found = True
    while p <= n and found:
        k = 1
        while (i + p*k) < len(arr):
            arr[i + p*k] = 0
            k += 1
        found = False
        j = i+1
        while (j < i + p) and j < len(arr):
            if arr[j] > 0:
                i = j
                p = arr[i]
                found = True
                break
            j += 1

    primes = [p for p in arr if p > 0]
    return primes

if __name__ == '__main__':
    for n in range(1, 51):
        print(2*n, prime_components(2*n))
