"""
    Given the root of a binary search tree, and a target k,
    return two nodes in the tree whose sum equals k.

    For example, given the following tree and k of 20

    10
   /   \
 5      15
       /  \
     11    15
    Return the nodes 5 and 15
"""
from collections import deque

"""
    Runs in O(n log(n)) time.
"""
def find_nodes_with_sum_k(root, k):
    q = deque([root])
    while len(q) > 0:
        node_1 = q.popleft()
        node_2 = find_helper(root, node_1, k - node_1.val)
        if node_2 != None:
            return (node_1.val, node_2.val)
        if node_1.left != None:
            q.append(node_1.left)
        if node_1.right != None:
            q.append(node_1.right)
    return None

def find_helper(root, node, val):
    if root.val == val and root != node:
        return root
    if val < root.val and (root.left != None):
        return find_helper(root.left, node, val)
    elif val >= root.val and (root.right != None):
        return find_helper(root.right, node, val)
    return None

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create_tree():
    node_5 = Node(5)
    node_10 = Node(10)
    node_11 = Node(11)
    node_15_1 = Node(15)
    node_15_2 = Node(15)

    node_10.left = node_5
    node_10.right = node_15_1
    node_15_1.left = node_11
    node_15_1.right = node_15_2

    return node_10

if __name__ == '__main__':
    root = create_tree()
    for summ in [10, 15, 16, 20, 21, 25, 26, 30, 31]:
        print('sum:', summ, find_nodes_with_sum_k(root, summ))
