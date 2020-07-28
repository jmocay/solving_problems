class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_swap_every_two_nodes(head):
    curr = head
    while curr != None and curr.next != None:
        tmp = curr.val
        curr.val = curr.next.val
        curr.next.val = tmp
        curr = curr.next.next
    return head

"""
    Print every element of the linked list
"""
def print_linked_list(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next

"""
    1 -> 2 -> 3 -> 4
"""
def test_linked_list_swap_every_two_nodes():
    head = Node(1)
    curr = head
    for k in (2, 3, 4, 5, 6, 7, 8, 9, 10):
        curr.next = Node(k)
        curr = curr.next
    print_linked_list(head)
    print("")
    head = linked_list_swap_every_two_nodes(head)
    print_linked_list(head)

if __name__ == '__main__':
    test_linked_list_swap_every_two_nodes()