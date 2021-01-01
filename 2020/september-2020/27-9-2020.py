"""
Evaluate Division
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        N = len(equations)
        for x in range(N):
            graph[equations[x][0]][equations[x][1]] = values[x]
            graph[equations[x][1]][equations[x][0]] = 1 / values[x]

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1

            if y in graph[x]:
                return graph[x][y]

            for tmp in graph[x]:
                if tmp not in visited:
                    visited.append(tmp)
                    val = dfs(tmp, y, visited)
                    if val == -1:
                        continue
                    else:
                        return val * graph[x][tmp]
            return -1

        result = []
        for query in queries:
            result.append(dfs(query[0], query[1], []))
        return result
