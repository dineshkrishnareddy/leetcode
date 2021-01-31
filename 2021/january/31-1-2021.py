"""
Next Permutation
https://leetcode.com/problems/next-permutation/
"""


class Solution:
    def nextPermutation(self, nums):
        def reverse(L, start, end):
            while start < end:
                L[start], L[end] = L[end], L[start]
                start, end = start + 1, end - 1

        i, n = len(nums) - 1, len(nums)
        while i >= 1 and nums[i] <= nums[i - 1]:
            i -= 1

        if i != 0:
            j = i
            while j + 1 < n and nums[j + 1] > nums[i - 1]:
                j += 1

            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        reverse(nums, i, n - 1)


print(Solution().nextPermutation([1,4,2,3]))
