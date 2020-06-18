"""
    Determine whether a single linked list is a palindrome.

    For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""
def is_linked_list_palindrome(head):
    n = get_node_count(head)

    # Split the linked list
    head1, head2tmp = reverse_half_linked_list(head, n // 2)
    head2 = head2tmp.next if (n % 2) > 0 else head2tmp

    # Compare the two linked list
    curr1 = head1
    curr2 = head2
    while curr1 != None and curr2 != None and curr1.val == curr2.val:
        curr1 = curr1.next
        curr2 = curr2.next
    if curr1 == None and curr2 == None:
        is_palindrome = True
    else:
        is_palindrome = False

    # Reverse the first linked list and re-attached to the second
    head1, head2 = reverse_half_linked_list(head1, n // 2)
    curr = head1
    while curr.next != None:
        curr = curr.next
    curr.next = head2tmp

    return is_palindrome

def get_node_count(head):
    n = 0
    while head != None:
        n += 1
        head = head.next
    return n

def create_linked_list(arr):
    head = None
    curr = None
    for i in arr:
        if head == None:
            head = Node(i)
            curr = head
        else:
            curr.next = Node(i)
            curr = curr.next
    return head

def reverse_half_linked_list(head, n):
    prev = None
    curr = head
    for i in range(n):
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev, curr

# For debugging only
def linked_list_to_string(head):
    arr = []
    while head != None:
        arr.append(head.val)
        head = head.next
    return str(arr)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == '__main__':
    print(is_linked_list_palindrome(create_linked_list('xabcdyydcbax')))
    print(is_linked_list_palindrome(create_linked_list('xabcdyxydcbax')))
    print(is_linked_list_palindrome(create_linked_list('xabcdxyzdcbax')))
    print(is_linked_list_palindrome(create_linked_list('xabcdxzdcbax')))
