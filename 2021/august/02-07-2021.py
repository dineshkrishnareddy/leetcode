"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique = {}
        for index, num in enumerate(nums):
            if num in unique:
                return [unique[num], index]
            else:
                unique[target - num] = index
        return None
