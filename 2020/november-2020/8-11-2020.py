"""
Binary Tree Tilt
https://leetcode.com/problems/binary-tree-tilt/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.tilt = 0

    def traverse(self, root):
        if root is None:
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val

    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.traverse(root)
        return self.tilt
