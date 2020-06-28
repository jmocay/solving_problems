"""
    Given a string of words delimited by spaces, reverse the words in string.
    For example, given "hello world here", return "here world hello"

    Follow-up: given a mutable string representation,
    can you perform this operation in-place?
"""
def reverse_words(arr):
    reverse(arr, 0, len(arr) - 1)
    begin = 0
    while begin < len(arr):
        # move begin to the first word character
        while arr[begin] == ' ':
            begin += 1
        if not begin < len(arr):
            break
        end = begin
        # move end to the pass the last word character
        while end < len(arr) and arr[end] != ' ':
            end += 1
        reverse(arr, begin, end-1)
        begin = end + 1

def reverse(arr, begin, end):
    arr_len = end - begin + 1
    mid = arr_len // 2
    for i in range(mid):
        tmp = arr[begin+i]
        arr[begin+i] = arr[end-i]
        arr[end-i] = tmp

def test_reverse_words():
    for s in [
        'the quick brown fox jumps over the lazy dog',
        'she sells sea shells by the sea shore',
        'the rain in Spain stays mainly in the plain',
        'Sinful Caesar sniffed his snifter seized his knees and sneezed',
        'In Hartford Hereford and Hampshire hurricanes hardly ever happen',
        'How kind of you to let me come',
        'Chester chooses chestnuts cheddar cheese with chewy chives',
        'He chews them and he chooses them',
        'He chooses them and he chews them',
        'Those chestnuts cheddar cheese and chives in cheery charming chunks',
        'Moses supposes his toes are the roses',
    ]:
        arr = [c for c in s]
        print(''.join(arr))
        reverse_words(arr)
        print(''.join(arr))
        print('')

if __name__ == '__main__':
    test_reverse_words()