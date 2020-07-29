"""
    Given a binary tree where all nodes are either 0 or 1,
    prune the tree so that subtrees containing all 0s are removed.

    For example, given the following tree:

      0
     / \
    1   0
       / \
      1   0
     / \
    0   0
    should be pruned to:

      0
     / \
    1   0
       /
      1
    We do not remove the tree at the root or its left child because it still has a 1
    as a descendant.
"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_tree_prune_zeros(root):
    prune_helper(root)
    if is_zero_leaf(root):
        del root
        return None
    return root

def prune_helper(root):
    if root.left != None:
        prune_helper(root.left)
        if is_zero_leaf(root.left):
            del root.left
            root.left = None
    if root.right != None:
        prune_helper(root.right)
        if is_zero_leaf(root.right):
            del root.right
            root.right = None

def is_zero_leaf(node):
    return node.val == 0 and node.left == None and node.right == None

"""
      0
     / \
    1   0
       / \
      1   0
     / \
    0   0

"""
from collections import deque
def print_binary_tree(root):
    if root == None:
        return
    q = deque([root])
    while len(q) > 0:
        node = q.popleft()
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
        print('id: {0} key: {1} left: {2} right: {3}'.format(
                id(node), node.val,
                'None' if node.left == None else id(node.left),
                'None' if node.right == None else id(node.right)
            )
        )

def test_binary_tree_prune_zeros():
    curr = Node(0)
    root = curr
    curr.left = Node(1)
    curr.right = Node(0)
    curr = curr.right
    curr.left = Node(1)
    curr.right = Node(0)
    curr = curr.left
    curr.left = Node(0)
    curr.right = Node(0)
    print_binary_tree(root)

    print("")

    root = binary_tree_prune_zeros(root)
    print_binary_tree(root)

if __name__ == '__main__':
    test_binary_tree_prune_zeros()