"""
Minimum Operations to Make Array Equal
https://leetcode.com/problems/minimum-operations-to-make-array-equal/
"""


class Solution:
    def minOperations(self, n: int) -> int:
        ele = [(2 * a) + 1 for a in range(n)]
        target = sum(ele) // n
        return sum([abs(a - target) for a in ele]) // 2
