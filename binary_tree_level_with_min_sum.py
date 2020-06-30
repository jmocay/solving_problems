"""
    Given a binary tree, return the level of the tree with minimum sum.
"""
def level_with_min_sum(root):
    level_sum = {}
    level = -1
    visit(root, level, level_sum)
    min_level, min_sum = get_min_level_sum(level_sum)
    return min_level

def visit(node, level, level_sum):
    level += 1
    if not level in level_sum:
        level_sum[level] = node.val
    else:
        level_sum[level] += node.val
    if node.left != None:
        visit(node.left, level, level_sum)
    if node.right != None:
        visit(node.right, level, level_sum)

def get_min_level_sum(level_sum):
    min_sum = None
    min_level = None
    for item in level_sum.items():
        if min_level == None or item[1] < min_sum:
            min_level = item[0]
            min_sum = item[1]
    return min_level, min_sum

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
                        10          = 10
                    6       7       = 13
                  4   5       8     = 17
                3       2   9   1   = 15

"""
if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_9 = Node(9)
    node_10 = Node(10)

    node_10.left = node_6
    node_10.right = node_7

    node_6.left = node_4
    node_6.right = node_5

    node_7.right = node_8

    node_4.left = node_3

    node_5.right = node_2

    node_8.left = node_9
    node_8.right = node_1

    print(level_with_min_sum(node_10))
