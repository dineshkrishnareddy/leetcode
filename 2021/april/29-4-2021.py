"""
Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(tar, arr, left=0):
            right = len(arr) - 1
            while left <= right:
                mid = left + right >> 1
                if arr[mid] < tar:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        left = find(target, nums)
        if left == len(nums) or nums[left] != target: return [-1, -1]
        return [left, find(target + 1, nums, left) - 1]
