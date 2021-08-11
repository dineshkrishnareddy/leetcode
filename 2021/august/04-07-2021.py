"""
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        result = []

        def dfs(root, path):
            if root is None:
                return
            if root.left is None and root.right is None:
                path.append(root.val)
                if sum(path) == targetSum:
                    result.append(path[:])
                path.pop()
                return
            path.append(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, [])
        return result
