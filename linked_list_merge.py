"""
    Given 2 sorted linked list, merge them into
    a single sorted linked list.
"""
class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_linked_list(head1, head2):

    head = None

    while head1 != None and head2 != None:
        if head1.val < head2.val:
            if head == None:
                head = LinkedListNode(head1.val)
                curr = head
            else:
                curr.next = LinkedListNode(head1.val)
                curr = curr.next
            head1 = head1.next
        else:
            if head == None:
                head = LinkedListNode(head2.val)
                curr = head
            else:
                curr.next = LinkedListNode(head2.val)
                curr = curr.next
            head2 = head2.next

    while head1 != None:
        if head == None:
            head = LinkedListNode(head1.val)
            curr = head
        else:
            curr.next = LinkedListNode(head1.val)
            curr = curr.next
        head1 = head1.next

    while head2 != None:
        if head == None:
            head = LinkedListNode(head2.val)
            curr = head
        else:
            curr.next = LinkedListNode(head2.val)
            curr = curr.next
        head2 = head2.next

    return head

def print_linked_list(head):
    arr = []
    while head != None:
        arr.append(head.val)
        head = head.next
    print(arr)

if __name__ == '__main__':
    n = 10

    head1 = None
    for i in range(n):
        if head1 == None:
            head1 = LinkedListNode(2*i + 1)
            curr = head1
        else:
            curr.next = LinkedListNode(2*i + 1)
            curr = curr.next

    head2 = None
    for i in range(n):
        if head2 == None:
            head2 = LinkedListNode(2*i + 2)
            curr = head2
        else:
            curr.next = LinkedListNode(2*i + 2)
            curr = curr.next

    print_linked_list(head1)
    print_linked_list(head2)

    head = merge_linked_list(head1, head2)
    print_linked_list(head)
