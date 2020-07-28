class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

"""
    Solution #1: Swapping the values
"""
def linked_list_swap_every_two_nodes_by_val(head):
    curr = head
    while curr != None and curr.next != None:
        tmp = curr.val
        curr.val = curr.next.val
        curr.next.val = tmp
        curr = curr.next.next
    return head

"""
    Solution #2: Swapping the next reference
"""
def linked_list_swap_every_two_nodes(head):
    curr = head
    head = None
    prev = None
    while curr != None and curr.next != None:
        curr_next = curr.next
        curr_next_next = curr.next.next
        curr.next = curr_next_next
        curr_next.next = curr
        if prev != None:
            prev.next = curr_next
        prev = curr
        if head == None:
            head = curr_next
        curr = curr_next_next
    if head == None:
        head = curr
    return head

"""
    Print every element of the linked list
"""
def print_linked_list(head):
    vals = []
    curr = head
    while curr != None:
        vals.append(curr.val)
        curr = curr.next
    print(' -> '.join(str(val) for val in vals))


"""
    Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5 -> 8 -> 7 -> 10 -> 9
"""
def test_linked_list_swap_every_two_nodes():
    head = Node(1)
    curr = head
    for k in range(2, 11):
        curr.next = Node(k)
        curr = curr.next
    print_linked_list(head)
    print("")
    head = linked_list_swap_every_two_nodes(head)
    print_linked_list(head)

if __name__ == '__main__':
    test_linked_list_swap_every_two_nodes()
