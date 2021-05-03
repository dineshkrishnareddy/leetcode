"""
Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index, num in enumerate(nums[1:], start=1):
            nums[index] = nums[index] + nums[index - 1]
        return nums
