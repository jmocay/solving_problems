def linked_list_rotate_right(llist, k):
    if llist.size == 0 or k % llist.size == 0:
        return
        
    last = llist.head
    while last.next != None:
        last = last.next
    last.next = llist.head

    nshift = k % llist.size
    prev = None
    curr = llist.head
    for i in range(llist.size - nshift):
        prev = curr
        curr = curr.next
    llist.head = curr
    prev.next = None

"""
  Ex:
    llist = 1, 2, 3; k=1
        3, 1, 2
    llist = 1, 2, 3; k=2
        2, 3, 1
    llist = 1, 2, 3; k=3
        1, 2, 3
  Therefore, when k == llist.size, llist remains the same
  Rotate right k times, shift the list k % llist.size times.
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def insert(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node
        self.size += 1

def print_linked_list(llist):
    arr = []
    curr = llist.head
    while curr != None:
        arr.append(curr.val)
        curr = curr.next
    print(arr)

def test_linked_list_rotate_right():
    llist = SingleLinkedList()
    for i in range(1, 11):
        llist.insert(i)
    print_linked_list(llist)
    linked_list_rotate_right(llist, 19)
    print_linked_list(llist)

if __name__ == '__main__':
    test_linked_list_rotate_right()
