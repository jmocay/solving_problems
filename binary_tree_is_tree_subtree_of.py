"""
    Given two non-empty binary trees s and t,
    check whether tree t has exactly the same structure
    and node values with a subtree of s.

    A subtree of s is a tree consists of a node in s and all of this node's descendants.
    The tree s could also be considered as a subtree of itself.
"""
from collections import deque

def is_tree_subtree_of(t, s):
    if not t == None and s == None:
        return False
    node = get_subtree_root(t, s)
    if node == None:
        return False
    # Level order traversal of t and subtree of s
    # rooted at node and compare node by node
    q_sub = deque([t])
    q_tree = deque([node])
    while len(q_sub) > 0 and len(q_tree) > 0:
        node_sub = q_sub.popleft()
        node_tree = q_tree.popleft()
        if node_sub.val != node_tree.val:
            return False
        if node_sub.left != None:
            q_sub.append(node_sub.left)
        if node_sub.right != None:
            q_sub.append(node_sub.right)
        if node_tree.left != None:
            q_tree.append(node_tree.left)
        if node_tree.right != None:
            q_tree.append(node_tree.right)
    if len(q_sub) > 0 and len(q_tree) == 0:
        return False
    else:
        return True

def get_subtree_root(root_sub, root):
    if root_sub.val == root.val:
        return root
    elif root_sub.val < root.val and root.left != None:
        return get_subtree_root(root_sub, root.left)
    elif root_sub.val > root.val and root.right != None:
        return get_subtree_root(root_sub, root.right)
    else:
        return None

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
          10
        7    11
      5   8    14
    4       9    18
               17  19
"""
def create_tree():
    node_7 = create_subtree()
    node_10 = Node(10)
    node_11 = Node(11)
    node_14 = Node(14)
    node_17 = Node(17)
    node_18 = Node(18)
    node_19 = Node(19)
    node_10.left = node_7
    node_10.right = node_11
    node_11.right = node_14
    node_14.right = node_18
    node_18.left = node_17
    node_18.right = node_19
    return node_10

"""
        7
      5   8
    4       9
"""
def create_subtree():
    node_4 = Node(4)
    node_5 = Node(5)
    node_7 = Node(7)
    node_8 = Node(8)
    node_9 = Node(9)
    node_7.left = node_5
    node_7.right = node_8
    node_5.left = node_4
    node_8.right = node_9
    return node_7

if __name__ == '__main__':
    root = create_tree()
    root_sub = create_subtree()
    print(is_tree_subtree_of(root_sub, root))
