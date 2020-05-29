"""
    Given the root of a binary tree, return a deepest node.
    For example, in the following tree, return e.
           a
         b   c
       d   e
              f
"""

class Node(object):

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
        return 'key: {0}, left: {1}, right: {2}'.format(
            key,
            'None' if self.left == None else self.left.key,
            'None' if self.right == None else self.right.key)

def find_deepest_node(root):
    if root == None:
        return None
    deepest = {
        "max_depth": -1,
        "depth": -1,
    }
    visit(root, deepest)
    return deepest["key"]

def visit(node, deepest):
    deepest["depth"] += 1
    if deepest["depth"] > deepest["max_depth"]:
        deepest["max_depth"] = deepest["depth"]
        deepest["key"] = node.key
    if node.left != None:
        visit(node.left, deepest)
    if node.right != None:
        visit(node.right, deepest)
    deepest["depth"] -= 1

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
    e.right = f
    deepest = find_deepest_node(a)
    print(deepest)
