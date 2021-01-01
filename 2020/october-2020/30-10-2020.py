"""
Number of Longest Increasing Subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0:
            return 0

        max_length = [1] * length
        max_count = [1] * length
        maxi = 1

        for j in range(1, length):
            for i in range(j):
                if nums[j] > nums[i]:
                    if max_length[i] + 1 > max_length[j]:
                        max_length[j] = max_length[i] + 1
                        max_count[j] = max_count[i]
                    elif max_length[i] + 1 == max_length[j]:
                        max_count[j] += max_count[i]
            maxi = max(maxi, max_length[j])

        print(max_length)
        print(max_count)
        print(maxi)
        result = 0
        for i in range(length):
            if max_length[i] == maxi:
                result += max_count[i]
        return result