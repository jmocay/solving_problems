"""
    A rule looks like this:
        A NE B
    means this means point A is located northeast of point B.

        A SW C
    means that point A is southwest of C.

    Given a list of rules, check if the sum of the rules validate.
    For example:
        A N B
        B NE C
        C N A
    does not validate, since A cannot be both north and south of C.

        A NW B
        A N B
    is considered valid
"""
def is_valid_bearing(rules):
    graph = build_graph(rules)
    return graph != None and not has_cycle(graph)

class Node(object):
    def __init__(self, nodeId):
        self.nodeId = nodeId
        self.north = {}
        self.south = {}
        self.east = {}
        self.west = {}

    def __str__(self):
        return '{0}, north: {1}, south: {2}, east: {3}, west: {4}'.format(
            self.nodeId,
            [neighId for neighId in self.north.keys()],
            [neighId for neighId in self.south.keys()],
            [neighId for neighId in self.east.keys()],
            [neighId for neighId in self.west.keys()],
        )

"""
    Builds a graph based on the input rules. Returns None if conflicting rules
    is detected, returns the populated graph otherwise.
"""
def build_graph(rules):
    graph = {}
    for rule in rules:
        rulTerm = rule.split(' ')
        if len(rulTerm) != 3: # disregard
            continue

        nodeId = rulTerm[0]
        if nodeId in graph:
            node = graph[nodeId]
        else:
            node = Node(nodeId)
            graph[nodeId] = node

        neighId = rulTerm[2]
        if neighId in graph:
            neighbor = graph[neighId]
        else:
            neighbor = Node(neighId)
            graph[neighId] = neighbor

        for direction in rulTerm[1]:
            if direction == 'N':
                if neighId in node.north:
                    return None
                node.south[neighId] = None
                neighbor.north[nodeId] = None
            elif direction == 'S':
                if neighId in node.south:
                    return None
                node.north[neighId] = None
                neighbor.south[nodeId] = None
            elif direction == 'E':
                if neighId in node.east:
                    return None
                node.west[neighId] = None
                neighbor.east[nodeId] = None
            elif direction == 'W':
                if neighId in node.west:
                    return None
                node.east[neighId] = None
                neighbor.west[nodeId] = None
    return graph

def has_cycle(graph):
    for nodeId in graph.keys():
        for direction in ['north', 'south', 'east', 'west']:
            if has_cycle_from_node(nodeId, graph, direction):
                return True
    return False

def has_cycle_from_node(searchId, graph, direction):
    visited = {}
    nodeId = searchId
    return has_cycle_from_node_helper(searchId, nodeId, graph, direction, visited)

"""
    Recursive depth-first-search depth-first search
"""
def has_cycle_from_node_helper(searchId, nodeId, graph, direction, visited):
    for neighId in graph[nodeId].__getattribute__(direction).keys():
        if neighId in visited:
            continue
        visited[neighId] = None
        if searchId == neighId:
            return True
        return has_cycle_from_node_helper(searchId, neighId, graph, direction, visited)

if __name__ == '__main__':
    print(
        'Valid' if is_valid_bearing([
            'A N B',
            'B NE C',
            'C N A'
        ]) else 'Invalid'
    )

    print(
        'Valid' if is_valid_bearing([
            'A NW B',
            'A N B'
        ]) else 'Invalid'
    )
