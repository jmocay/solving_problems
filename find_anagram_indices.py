"""
    Given a word W and a string S, find all starting indices in S which are anagrams of W.

    For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

def find_anagram_indices(W, S):
    idx = []
    if len(W) > len(S):
        return tuple(idx)
    lkp_w = {}
    for w in W:
        lkp_w[w] = None

    for i in range(len(S)-len(W)+1):
        lkp_s = {}
        for s in S[i:i+len(W)]:
            lkp_s[s] = None
        not_anagram = False
        for w in lkp_w.keys():
            if w not in lkp_s:
                not_anagram = True
                break
        if not_anagram:
            continue
        for s in lkp_s.keys():
            if s not in lkp_w:
                not_anagram = True
                break
        if not_anagram:
            continue
        idx.append(i)

    return tuple(idx)

if __name__ == '__main__':
    print(find_anagram_indices('ab', 'abxaba'))