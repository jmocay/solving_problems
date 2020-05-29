"""
    Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
    A 1 represents land and 0 represents water, so an island is a group of 1's
    that are neighboring whose perimeter is surrounded by water.
"""

def islands_in_2darray(arr):
    n = 0

    graph = build_graph(arr)

    in_island = {} # stores nodes that are already marked as part of an island

    for key in graph:
        node = graph[key]
        if is_new_island(node, in_island):
            n += 1

    return n

"""
    Graph node:
        key contains the row,col indices of the non-zero element of an array

"""
class Node(object):
    def __init__(self, row, col):
        self.key = '{0}|{1}'.format(row, col)
        self.neighbors = {}
    def __str__(self):
        return '{0} -> {1}'.format(
            self.key,
            [neighbor for neighbor in self.neighbors.keys()]
        )

def build_graph(arr):
    graph = {}

    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == 1:
                key = '{0}|{1}'.format(row, col)
                node = None
                if not key in graph:
                    node = Node(row, col)
                    graph[key] = node
                else:
                    node = graph[key]
                for i in range(row-1, row+2):
                    if i < 0 or i == len(arr):
                        continue
                    for j in range(col-1, col+2):
                        if j < 0 or j == len(arr[i]) or (i==row and j==col) or arr[i][j] == 0:
                            continue
                        nkey = '{0}|{1}'.format(i, j)
                        neighbor = None
                        if not nkey in graph:
                            neighbor = Node(i, j)
                            graph[nkey] = neighbor
                        else:
                            neighbor = graph[nkey]
                        if not nkey in node.neighbors:
                            node.neighbors[nkey] = neighbor
                        if not key in neighbor.neighbors:
                            neighbor.neighbors[key] = node

    return graph

def is_new_island(node, in_island):
    if node.key in in_island:
        return False
    visited = {} # stores nodes already visited by the dfs
    dfs(node, visited, in_island)
    return True

def dfs(node, visited, in_island):
    in_island[node.key] = 0 # add the node and it's neighbors to in_island
    visited[node.key] = 0   # just store the key
    for key in node.neighbors:
        if key in visited:
            continue
        neighbor = node.neighbors[key]
        dfs(neighbor, visited, in_island)

if  __name__ == '__main__':
    # 4 islands
    arr4 = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    # five islands
    arr5 = [
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    # six islands
    arr6 = [
        [1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    graph = build_graph(arr4)
    print(islands_in_2darray(arr4))

    graph = build_graph(arr5)
    print(islands_in_2darray(arr5))

    graph = build_graph(arr6)
    print(islands_in_2darray(arr6))
