from collections import deque

"""
    Invert a binary tree.
    For example, given the binary tree:
           a
        b      c
      d   e  f
    should become:
           a
        c      b
          f  e   d
"""

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def invert_binary_tree(root):
    if root == None:
        return

    que = deque()
    que.append(root)

    while len(que) > 0:
        node = que.popleft()
        tmp = node.left
        node.left = node.right
        node.right = tmp
        if node.left != None:
            que.append(node.left)
        if node.right != None:
            que.append(node.right)

"""
    Test
"""
def print_binary_tree(root):
    if root == None:
        return

    keys = []
    que = deque()
    que.append(root)

    while len(que) > 0:
        node = que.popleft()
        keys.append(node.key)
        if node.left != None:
            que.append(node.left)
        if node.right != None:
            que.append(node.right)
    print(keys)

if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    print_binary_tree(a)
    invert_binary_tree(a)
    print_binary_tree(a)
