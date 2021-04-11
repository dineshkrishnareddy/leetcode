"""
Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_max_depth(self, root, level):
        if not root:
            return level

        return max(self.get_max_depth(root.left, level + 1), self.get_max_depth(root.right, level + 1))

    def get_level_sum(self, root, depth):
        if not root:
            return 0

        if depth == 0:
            return root.val

        return sum([self.get_level_sum(root.left, depth - 1), self.get_level_sum(root.right, depth - 1)])

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_depth = self.get_max_depth(root, 0)
        return self.get_level_sum(root, max_depth - 1)
