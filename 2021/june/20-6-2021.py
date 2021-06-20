"""
778. Swim in Rising Water
https://leetcode.com/problems/swim-in-rising-water/
"""
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        length = len(grid)
        ans = 0
        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        while pq:
            value, row, col = heapq.heappop(pq)
            ans = max(ans, value)
            if row == col == length - 1:
                return ans
            for new_row, new_col in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= new_row <= length - 1 and 0 <= new_col <= length - 1 and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    heapq.heappush(pq, (grid[new_row][new_col], new_row, new_col))
