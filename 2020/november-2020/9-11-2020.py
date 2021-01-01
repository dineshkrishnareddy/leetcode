"""
Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_diff = 0

    def get_max_diff(self, root, arr):
        if root is None:
            self.max_diff = max(self.max_diff, abs(max(arr) - min(arr)))
            return
        arr.append(root.val)
        self.get_max_diff(root.left, arr)
        self.get_max_diff(root.right, arr)
        arr.pop()

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.get_max_diff(root, [])
        return self.max_diff
