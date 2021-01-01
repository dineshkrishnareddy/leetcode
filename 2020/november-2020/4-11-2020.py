"""
Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        leaves = [i for i in graph.keys() if len(graph[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leaf in leaves:
                neighbour = graph[leaf].pop()
                graph[neighbour].remove(leaf)

                if len(graph[neighbour]) == 1:
                    new_leaves.add(neighbour)
            leaves = new_leaves
        return leaves
