"""
    Given a string, determine whether any permutation of it is a palindrome.

    For example,
        'carrace' should return true, since it can be rearranged to form 'racecar',
        which is a palindrome.
        'daily' should return false, since there's no rearrangement that can form a palindrome.
"""
def string_has_palindrome_permutation(string):
    chars = {}
    for c in string:
        if c not in chars or chars[c] == 0:
            chars[c] = 1
        else:
            chars[c] -= 1
    no_pair_cnt = sum(cnt for cnt in chars.values())
    return no_pair_cnt == 0 or no_pair_cnt == 1

if __name__ == '__main__':
    for string in [
        'carrace',
        'daily',
        'yoyoma',
        'person',
        'man',
        'woman',
        'camera',
        'tv',
        'catacamat'
    ]:
        print(string, string_has_palindrome_permutation(string))
