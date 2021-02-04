"""
Longest Harmonious Subsequence
https://leetcode.com/problems/longest-harmonious-subsequence/
"""


class Solution:

    def findLHS(self, nums):
        from collections import Counter
        c = Counter(nums)
        return max([c[k] + c[k - 1] for k in c if k - 1 in c])


print(Solution().findLHS([1,3,2,2,5,2,3,7]))
