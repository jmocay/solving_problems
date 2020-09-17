"""
Given the root of a binary tree, find the most frequent subtree sum.
The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

      5
     / \
    2  -5

Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5
"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def most_frequent_subtree_sum(root):
    subtree_sum(root)
    sdict = {}
    most_frequent_subtree_sum_helper(root, sdict)
    csum, sum_cnt = (0, 0)
    for item in sdict.items():
        if item[1] > sum_cnt:
            csum = item[0]
            sum_cnt = item[1]
    return csum

def subtree_sum(root):
    if root == None:
        return 0
    left = subtree_sum(root.left)
    right = subtree_sum(root.right)
    root.subtree_sum = root.val + left + right
    return root.subtree_sum

def most_frequent_subtree_sum_helper(root, sdict):
    if root == None:
        return
    if root.subtree_sum in sdict:
        sdict[root.subtree_sum] += 1
    else:
        sdict[root.subtree_sum] = 1
    most_frequent_subtree_sum_helper(root.left, sdict)
    most_frequent_subtree_sum_helper(root.right, sdict)

def test_most_frequent_subtree_sum():
    root = Node(5)
    root.left = Node(2)
    root.right = Node(-5)
    print(subtree_sum(root))
    print(subtree_sum(root.left))
    print(subtree_sum(root.right))
    print(most_frequent_subtree_sum(root))

if __name__ == '__main__':
    test_most_frequent_subtree_sum()
