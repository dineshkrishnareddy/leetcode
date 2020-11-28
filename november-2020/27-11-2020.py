"""
Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        count = sum(nums)
        length = len(nums)

        if count % 2 != 0:
            return False

        dp = [[False for j in range(count // 2 + 1)] for i in range(length + 1)]

        for i in range(1, length + 1):
            for j in range(1, count // 2 + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                elif nums[i - 1] == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[length][count // 2]
