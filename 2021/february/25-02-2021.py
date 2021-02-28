"""
Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        l = 1
        while l < n - 1 and nums[l] > nums[l - 1]:
            l += 1
        mn = min(nums[l:])

        r = n - 2
        while r >= 0 and nums[r] < nums[r + 1]:
            r -= 1
        mx = max(nums[r::-1])

        i = 0
        while i < n and nums[i] <= mn:
            i += 1

        j = n - 1
        while j >= 0 and nums[j] >= mx:
            j -= 1

        return j - i + 1 if j - i > 0 else 0
