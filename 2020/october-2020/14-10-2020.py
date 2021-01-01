"""
House Robber II
"""


class Solution:
    def get_max_robbed(self, nums):
        max1 = max2 = maxi = 0
        for index in range(len(nums)):
            maxi = max(max2 + nums[index], max1)
            max2 = max1
            max1 = maxi
        return maxi

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.get_max_robbed(nums[:-1]), self.get_max_robbed(nums[1:]))
