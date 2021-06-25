"""
684. Redundant Connection
https://leetcode.com/problems/redundant-connection/
"""
import collections


class Solution:

    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if v in graph and u in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
