"""
    Given a binary tree, find the lowest common ancestor (LCA)
    of two given nodes in the tree.
    Assume that each node in the tree also has a pointer to its parent.
"""
# First approach using list of ancestor nodes
def find_lowest_common_ancestor_node0(node1, node2):
    node1_ancestors = get_ancestors(node1)
    node2_ancestors = get_ancestors(node2)
    lca = None
    while len(node1_ancestors) > 0 and len(node2_ancestors) > 0:
        ancestor1 = node1_ancestors.pop()
        ancestor2 = node2_ancestors.pop()
        if ancestor1 != ancestor2:
            break
        else:
            lca = ancestor1
    return lca

def get_ancestors(node):
    ancestors = []
    while node.parent != None:
        ancestors.append(node.parent)
        node = node.parent
    return ancestors

# Second approach using dictionary
def find_lowest_common_ancestor_node(node1, node2):
    node1_ancestors = {}
    node = node1
    while node.parent != None:
        node1_ancestors[node.parent] = None
        node = node.parent
    lca = None
    node = node2
    while node.parent != None:
        if node.parent in node1_ancestors:
            lca = node.parent
            break
        node = node.parent
    return lca

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.key)
    def __repr__(self):
        return str(self)
"""
        1
      2   3
    4  5 6  7
   8 9       10
"""
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)

    node1.left = node2
    node1.right = node3
    node2.parent = node1
    node3.parent = node1

    node2.left = node4
    node2.right = node5
    node4.parent = node2
    node5.parent = node2

    node3.left = node6
    node3.right = node7
    node6.parent = node3
    node7.parent = node3

    node4.left = node8
    node4.right = node9
    node8.parent = node4
    node9.parent = node4

    node7.right = node10
    node10.parent = node7

    print("nodes:", node8, node9, "lca:", find_lowest_common_ancestor_node(node8, node9))
    print("nodes:", node8, node5, "lca:", find_lowest_common_ancestor_node(node8, node5))
    print("nodes:", node8, node10, "lca:", find_lowest_common_ancestor_node(node8, node10))
    print("nodes:", node6, node10, "lca:", find_lowest_common_ancestor_node(node6, node10))
    print("nodes:", node8, node4, "lca:", find_lowest_common_ancestor_node(node8, node4))
    print("nodes:", node8, node2, "lca:", find_lowest_common_ancestor_node(node8, node2))
    print("nodes:", node1, node10, "lca:", find_lowest_common_ancestor_node(node1, node10))