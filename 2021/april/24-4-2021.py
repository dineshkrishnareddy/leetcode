"""
Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/
"""


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        cons = defaultdict(set)
        for a, b in connections:
            cons[a].add(b)
            cons[b].add(a)

        low = {}
        results = []

        def visit(node, from_node=None):
            if node in low: return low[node]
            cur_id = low[node] = len(low)

            for neigh in cons[node]:
                if neigh == from_node: continue
                low[node] = min(low[node], visit(neigh, node))

            if cur_id == low[node] and from_node is not None:
                results.append([from_node, node])
            return low[node]

        visit(0)
        return results
