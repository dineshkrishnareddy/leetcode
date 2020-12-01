"""
Maximum Depth of Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depth(self, root):
        if root.left is None and root.right is None:
            return 1
        left = right = 0
        if root.left:
            left = self.depth(root.left)
        if root.right:
            right = self.depth(root.right)
        return max(left, right) + 1

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.depth(root)
