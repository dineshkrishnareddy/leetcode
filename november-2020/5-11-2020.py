"""
Minimum Cost to Move Chips to The Same Position
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if len(position) == 0:
            return 0

        even_count = 0
        odd_count = 0

        for p in position:
            if p % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return min(even_count, odd_count)
