"""
Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trim(self, root, low, high):
        if root is None:
            return None

        if low > root.val:
            return self.trim(root.right, low, high)

        if root.val > high:
            return self.trim(root.left, low, high)

        root.left = self.trim(root.left, low, high)
        root.right = self.trim(root.right, low, high)

        return root

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None

        return self.trim(root, low, high)
