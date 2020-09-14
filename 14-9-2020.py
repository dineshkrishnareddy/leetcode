"""
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]
        for index in range(2, len(nums)):
            if index < 3:
                dp[index] = nums[index] + dp[index - 2]
            else:
                dp[index] = max(nums[index] + dp[index - 2], nums[index] + dp[index - 3])

        return max(dp)
