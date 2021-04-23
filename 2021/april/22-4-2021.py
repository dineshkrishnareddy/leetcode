"""
Brick Wall
https://leetcode.com/problems/brick-wall/
"""
from itertools import accumulate
from collections import defaultdict


class Solution:
    def leastBricks(self, wall) -> int:
        edges, maxEdges = defaultdict(int), 0
        for row in wall:
            for idx in accumulate(row[:-1]):
                edges[idx] += 1
                maxEdges = max(maxEdges, edges[idx])
        return len(wall) - maxEdges


print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
