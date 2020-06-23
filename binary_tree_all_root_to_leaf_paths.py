"""
    Given a binary tree, return all paths from the root to leaves.

    For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
    Return [[1, 2], [1, 3, 4], [1, 3, 5]].    
"""
def get_all_root_to_leaf_paths(root):
    paths = []
    if root == None:
        return paths
    curr_path = []
    get_path(root, curr_path, paths)
    return paths

def get_path(root, curr_path, paths):
    curr_path.append(root.val)
    if root.left == None and root.right == None:
        path = [val for val in curr_path]
        paths.append(path)
        curr_path.pop()
        return
    if root.left != None:
        get_path(root.left, curr_path, paths)
    if root.right != None:
        get_path(root.right, curr_path, paths)
    curr_path.pop()

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self, val):
        return str(self.val)

"""
   1
  / \
 2   3
    / \
   4   5
"""
if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_1.left = node_2
    node_1.right = node_3
    node_3.left = node_4
    node_3.right = node_5
    paths = get_all_root_to_leaf_paths(node_1)
    print(paths)
