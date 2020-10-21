"""
Clone Graph
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        seen = {}

        def dfs(node, seen):
            new_node = Node(node.val)
            seen[node.val] = new_node
            new_neighbors = []

            for n in node.neighbors:
                if n.val not in seen:
                    new_neighbors.append(dfs(n, seen))
                else:
                    new_neighbors.append(seen[n.val])
            new_node.neighbors = new_neighbors
            return new_node

        return dfs(node, seen)
