"""
Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.traverse(root, low, high)
        return self.sum

    def traverse(self, root, low, high):
        if root is None:
            return 0

        if low <= root.val <= high:
            self.sum += root.val

        return self.traverse(root.left, low, high) + self.traverse(root.right, low, high)
