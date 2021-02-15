"""
Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/
"""

'''
w: Bipartite --> BFS + coloring
h: Use regular BFS manner to traverse the graph:
    1) each pair of connected nodes A--B cannot have same color
        we use 1 to mark A and -1 to mark B
    2) if we a node was seen before and the color does not match, 
        this means this node violate the bipartite condition
    3) repeat this process for all nodes since not all the nodes are connected, 
		in other words, the graph may have different disjoint components
'''
import collections


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        seen = {}
        for i in range(len(graph)):
            if i not in seen:
                queue = collections.deque([(i, 1)])
                while queue:
                    node, color = queue.popleft()
                    if node in seen:
                        if color == seen[node]:
                            continue
                        else:
                            return False
                    seen[node] = color

                    for nei in graph[node]:
                        queue.append((nei, color * (-1)))

        return True
