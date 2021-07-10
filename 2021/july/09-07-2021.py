"""
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        curr = 1
        while curr < length:
            start = 0
            while start < curr:
                if nums[start] < nums[curr]:
                    dp[curr] = max(dp[curr], dp[start] + 1)
                start += 1
            curr += 1
        return max(dp)
