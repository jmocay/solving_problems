"""
    Print the nodes in a binary tree level-wise.
    For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""
from collections import deque

def print_binary_tree_level_order(root):
    if root == None:
        return
    q = deque([root])
    arr = []
    while len(q) > 0:
        node = q.popleft()
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
        arr.append(str(node))
    print(', '.join(arr))

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

if __name__ == '__main__':
    def create_tree():
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        one.left = two
        one.right = three
        three.left = four
        three.right = five
        return one
    print_binary_tree_level_order(create_tree())