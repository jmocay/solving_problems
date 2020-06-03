"""
    Given a singly linked list and an integer k,
    remove the kth last element from the list.
    k is guaranteed to be smaller than the length of the list.

    Note: The list is very long, so making more than one pass is prohibitively expensive.

    Do this in constant space and in one pass.
"""
def remove_element_from_last(head, k):
    prev = None
    curr = head

    # Advance the last ahead of curr by k
    last = head
    for i in range(k):
        last = last.next

    # Advance the last to one after the last node
    while last != None:
        if prev == None:
            prev = head
        else:
            prev = prev.next
        curr = curr.next
        last = last.next

    # curr remains the head, make the node next to head as new head
    if curr == head:
        head = head.next
        del curr
        return head
    else:
        prev.next = curr.next
        del curr
        return head

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)

def create_linked_list(n):
    head = Node(1)
    curr = head
    for i in range(1, n):
        curr.next = Node(i+1)
        curr = curr.next
    return head

def linked_list_to_string(head):
    vals = []
    curr = head
    while curr != None:
        vals.append(str(curr))
        curr = curr.next        
    return ', '.join(vals)

if __name__ == '__main__':
    # removind the beginning
    head = create_linked_list(5)
    print(linked_list_to_string(head))
    head = remove_element_from_last(head, 5)
    print(linked_list_to_string(head))

    # removing at the middle
    head = create_linked_list(10)
    print(linked_list_to_string(head))
    head = remove_element_from_last(head, 5)
    print(linked_list_to_string(head))

    # removing at the end
    head = create_linked_list(10)
    print(linked_list_to_string(head))
    head = remove_element_from_last(head, 1)
    print(linked_list_to_string(head))
