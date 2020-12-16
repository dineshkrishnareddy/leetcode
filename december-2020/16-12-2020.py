"""
Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, low, high):
        if root is None:
            return True

        if low < root.val < high:
            return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))
