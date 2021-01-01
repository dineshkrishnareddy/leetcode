"""
Squares of a Sorted Array
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])
