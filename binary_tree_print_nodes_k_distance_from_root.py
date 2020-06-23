"""
    Print nodes at k distance from root
    Given a root of a tree, and an integer k.
    Print all the nodes which are at k distance from root.
    For example, in the below tree, 4, 5 & 6 are at distance 2 from root.
            1
          /   \
        2      3
      /  \    /
    4     5  6
"""

def print_nodes_k_distance_from(root, k):
    if root == None:
        return
    d = -1
    print_k_distant_node(root, k, d)

def print_k_distant_node(root, k, d):
    d += 1
    if k == d:
        print(root.val)
        d -= 1
        return
    if root.left != None:
        print_k_distant_node(root.left, k, d)
    if root.right != None:
        print_k_distant_node(root.right, k, d)
    d -= 1
    return

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
            1
          /   \
        2      3
      /  \    /
    4     5  6
"""
if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.right = node_6

    for d in range(5):
        print("distance: {0}".format(d))
        print_nodes_k_distance_from(node_1, d)
