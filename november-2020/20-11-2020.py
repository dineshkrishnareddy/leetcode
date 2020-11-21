"""
Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return target in nums
        left, right = 0, len(nums) - 1
        while left <= right:
            m = left + right >> 1
            if nums[m] == target: return True

            while nums[left] == nums[m] == nums[right]:
                left += 1
                right -= 1
                if left > right: return False

            if (target < nums[left], target) < (nums[m] < nums[left], nums[m]):
                right = m - 1
            else:
                left = m + 1

        return False
