"""
    Determine whether there exists a one-to-one character mapping
    from one string s1 to another s2.

    For example, given s1 = abc and s2 = bcd,
    return true since we can map a to b, b to c, and c to d.

    Given s1 = foo and s2 = bar,
    return false since the o cannot map to two characters.
"""
def is_isomorphic(str1, str2):
    if len(str1) != len(str2): # base case
        return False
    cmap = {}
    for i, c in enumerate(str1):
        if not c in cmap:
            cmap[c] = str2[i] # or cmap[str1[i]] = str2[i]
            continue
        if cmap[c] != str2[i]:
            return False
    return True

def test_is_isomorphic():
    for pair in [
        ('a', 'bc'),
        ('ab', 'bc'),
        ('foo', 'bar'),
        ('abba', 'cxxc'),
    ]:
        print(pair[0], pair[1], 'is_isomorphic: ', is_isomorphic(pair[0], pair[1]))

if __name__ == '__main__':
    test_is_isomorphic()
