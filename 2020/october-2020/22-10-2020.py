"""
Minimum Depth of Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.depth(root)

    def depth(self, root: TreeNode) -> int:
        if root is None:
            return float("inf")

        if root.left is None and root.right is None:
            return 1

        return 1 + min(self.depth(root.left), self.depth(root.right))
