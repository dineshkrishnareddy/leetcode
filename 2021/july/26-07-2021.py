"""
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def convert(nums):
            if len(nums) == 0:
                return None
            low, high = 0, len(nums)
            mid = (high - low) // 2

            root = TreeNode(nums[mid])
            root.left = convert(nums[:mid])
            root.right = convert(nums[mid + 1:])
            return root

        return convert(nums)
