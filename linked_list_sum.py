"""
Let's represent an integer in a linked list format by having each node
represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

    1 -> 2 -> 3 -> 4 -> 5
    is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

    9 -> 9
    5 -> 2
    return 124 (99 + 25) as:

    4 -> 2 -> 1
"""
def linked_list_sum(nlist1, nlist2):
    curr1 = nlist1.head
    curr2 = nlist2.head
    slist = NumericLinkedList()
    carry = 0
    while curr1 != None and curr2 != None:
        total = curr1.val + curr2.val + carry
        carry = total // 10
        slist.add(total % 10)
        curr1 = curr1.next
        curr2 = curr2.next
    while curr1 != None:
        total = curr1.val + carry
        carry = total // 10
        slist.add(total % 10)
        curr1 = curr1.next
    while curr2 != None:
        total = curr2.val + carry
        carry = total // 10
        slist.add(total % 10)
        curr2 = curr2.next
    if carry > 0:
        slist.add(carry)
    return slist

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class NumericLinkedList(object):
    def __init__(self):
        self.head = None
    def add(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node
    def value(self):
        total = 0
        mult = 1
        curr = self.head
        while curr != None:
            total += mult * curr.val
            mult *= 10
            curr = curr.next
        return total

def create_linked_list(n):
    nlist = NumericLinkedList()
    while n > 0:
        nlist.add(n - 10*(n // 10))
        n = n // 10
    return nlist

if __name__ == '__main__':
    nlist1 = create_linked_list(99)
    nlist2 = create_linked_list(25)
    slist = linked_list_sum(nlist1, nlist2)
    print(nlist1.value(), nlist2.value(), slist.value())
