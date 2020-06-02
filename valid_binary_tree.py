from collections import deque

"""
    A binary search tree is a tree with two children, left and right,
    and satisfies the constraints that:
        the key in the left child must be less than or equal to the root and
        the key in the right child must be greater than or equal to the root.
"""
def is_valid_binary_tree(root):
    if root == None:
        return False
    que = deque([root])
    while len(que) > 0:
        node = que.pop()
        if node.left != None:
            if node.left.key > node.key:
                return False
            que.appendleft(node.left)
        if node.right != None:
            if node.right.key < node.key:
                return False
            que.appendleft(node.right)
    return True

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def __str__(self):
        return 'key: {0}, left: {1}, right: {2}'.format(
            self.key,
            'None' if self.left == None else str(self.left.key),
            'None' if self.right == None else str(self.right.key),
        )

if __name__ == '__main__':
    """
            d
        b      f
    a    c  e   g
    """
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    d.left = b
    d.right = f
    b.left = a
    b.right = c
    f.left = e
    f.right = g
    print('Valid' if is_valid_binary_tree(d) else 'Invalid')

    """
            d
        b      f
    a    c  g   e
    """
    f.left = g
    f.right = e
    print('Valid' if is_valid_binary_tree(d) else 'Invalid')