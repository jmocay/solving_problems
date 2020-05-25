"""
    Given a mapping of digits to letters (as in a phone number), and a digit string,
    return all possible letters the number could represent.
    You can assume each valid number in the mapping is a single digit.

    For example if {“2”: [“a”, “b”, “c”], "3": [“d”, “e”, “f”]},
    then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].


"""
def letter_combinations_from_digits_mapping(mapping, digits):
    alpha_strings = []
    if len(digits) == 0:
        return alpha_strings
    idx = len(digits) * [0]
    while idx[0] < len(mapping[digits[0]]):
        alpha_strings.append(''.join(mapping[digits[i]][idx[i]] for i in range(len(digits))))

        idx[len(digits) - 1] += 1
        i = len(digits) - 1
        while i > 0:
            if idx[i] == len(mapping[digits[i]]):
                idx[i] = 0
                idx[i - 1] += 1
            else:
                break
            i -= 1
    return alpha_strings

if __name__ == '__main__':
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"]
    }
    digits = "23"
    alpha_strings = letter_combinations_from_digits_mapping(mapping, digits)
    print(alpha_strings)