"""
    Given the head of a singly linked list, reverse it in-place.
"""

class LinkedListNode(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr != None:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

"""
  Utility function to convert linked list to an array
"""
def linked_list_to_array(head):
    arr = []
    curr = head
    while curr != None:
        arr.append(curr.val)
        curr = curr.next
    return arr

"""
  Utility function to create a linked list with n consecutive positive integers
"""
def create_linked_list(n):
    head = LinkedListNode(1)
    curr = head
    for i in range(2, n+1):
        curr.next = LinkedListNode(i)
        curr = curr.next
    return head

for n in range(1, 11):
    head = create_linked_list(n)
    arr = linked_list_to_array(head)
    print("original list:", arr)
    head = reverse_linked_list(head)
    arr = linked_list_to_array(head)
    print("reverse list:", arr)
