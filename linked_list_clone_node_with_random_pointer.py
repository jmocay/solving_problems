"""
    Given the head to a singly linked list,
    where each node also has a “random” pointer
    that points to anywhere in the linked list,
    deep clone the list.
"""
def clone_linked_list(src_list):
    dst_list = LinkedList()
    src = src_list.head
    n = 0
    while src != None:
        dst_list.add(Node(src.val))
        n += 1
        src = src.next
    src = src_list.head
    dst = dst_list.head
    while src != None and dst != None:
        src_rnd = src.random
        i = index_from_end(src_rnd)
        dst_rnd = kth_node(dst_list, n-i+1)
        dst.random = dst_rnd
        src = src.next
        dst = dst.next
    return dst_list

"""
    Index of node from the end of the list.
    The last node will have an index of 1.
"""
def index_from_end(node):
    k = 0
    while node != None:
        k += 1
        node = node.next
    return k

"""
    Return the kth node from the beginning of the list.
    The first node will have an index of 1.
"""
def kth_node(linked_list, k):
    if k < 1 or linked_list.head == None:
        return None
    i = 1
    node = linked_list.head
    while node != None and i < k:
        node = node.next
        i += 1
    return node

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    def add(self, node):
        if self.head == None:
            self.head = node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node

"""
    Test driver
"""
def create_test_linked_list():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    node_1.random = node_3
    node_2.random = node_4
    node_3.random = node_5
    node_4.random = node_1
    node_5.random = node_2

    src_list = LinkedList()
    src_list.head = node_1

    return src_list

def linked_list_to_tuple(linked_list):
    vals = []
    rnds = []
    node = linked_list.head
    while node != None:
        vals.append(node.val)
        rnds.append(node.random.val)
        node = node.next
    return (vals, rnds)

if __name__ == '__main__':
    src_list = create_test_linked_list()
    vals, rnds = linked_list_to_tuple(src_list)
    print('src vals:', vals)
    print('src rnds:', rnds)

    dst_list = clone_linked_list(src_list)
    vals, rnds = linked_list_to_tuple(dst_list)
    print('dst vals:', vals)
    print('dst rnds:', rnds)
