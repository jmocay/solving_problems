"""
    Given a string, return the first recurring character in it,
    or null if there is no recurring character.

    For example, given the string "acbbac", return "b".
    Given the string "abcdef", return null.
"""
def first_recurring_char(string):
    bmp = 0
    for c in string:
        n = ord(c.lower()) - ord('a')
        bit = (1 << n)
        if bmp & bit == 0:
            bmp |= bit
        else:
            return c
    return None

if __name__ == '__main__':
    for string in [
        'acbbac',
        'abcdef',
        'hello',
        'world',
        'abracadabra'
    ]:
        print(string, first_recurring_char(string))
