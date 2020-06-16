"""
    A unival tree (which stands for "universal value") is a tree
    where all nodes under it have the same value.

    Given the root to a binary tree, count the number of unival subtrees.

    For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
def count_unival_trees(root):
    (count, is_unival) = count_unival_trees_helper(root)
    return count

def count_unival_trees_helper(root):
    if root == None:
        return (0, False)
    (count_left, is_left_unival) = count_unival_trees_helper(root.left)
    (count_right, is_right_unival) = count_unival_trees_helper(root.right)
    if root.left != None and root.left.val == root.val and root.right != None and root.right.val == root.val:
        return (count_left + count_right + 1, True)
    elif root.left == None and root.right == None:
        return (1, True)
    else:
        return (count_left + count_right, False)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if __name__ == '__main__':
    a = Node(0)
    b = Node(1)
    c = Node(0)
    d = Node(1)
    e = Node(0)
    f = Node(1)
    g = Node(1)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    d.left = f
    d.right = g
    print(count_unival_trees(a))
