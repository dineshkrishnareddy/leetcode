"""
Beautiful Arrangement
https://leetcode.com/problems/beautiful-arrangement/
"""


class Solution:
    def countArrangement(self, n: int) -> int:
        @functools.cache
        def solve(cur):
            if len(cur) == 1:
                return 1

            total = 0
            for j in range(len(cur)):
                if cur[j] % len(cur) == 0 or len(cur) % cur[j] == 0:
                    total += solve(cur[:j] + cur[j + 1:])

            return total

        return solve(tuple(range(1, n + 1)))
