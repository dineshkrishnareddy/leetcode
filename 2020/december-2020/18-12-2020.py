"""
Increasing Triplet Subsequence
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left, mid = float('inf'), float('inf')

        for curr in nums:
            if curr > mid:
                return True
            elif left < curr < mid:
                mid = curr
            elif curr < left:
                left = curr
        return False
