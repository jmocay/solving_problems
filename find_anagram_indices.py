"""
    Given a word W and a string S, find all starting indices in S which are anagrams of W.

    For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

def find_anagram_indices(W, S):
    idx = []
    if len(W) > len(S):
        return tuple(idx)
    lkp_w = word2dict(W)

    for i in range(len(S)-len(W)+1):
        lkp_s = word2dict(S[i:i+len(W)])
        if not is_anagram(lkp_w, lkp_s):
            continue
        idx.append(i)

    return tuple(idx)

def word2dict(W):
    lkp = {}
    for w in W:
        lkp[w] = None
    return lkp

def is_anagram(lkp_w, lkp_s):
    for w in lkp_w.keys():
        if w not in lkp_s:
            return False
    for s in lkp_s.keys():
        if s not in lkp_w:
            return False
    return True

if __name__ == '__main__':
    print(find_anagram_indices('ab', 'abxaba'))