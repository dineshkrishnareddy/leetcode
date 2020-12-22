"""
Balanced Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balance(self, root):
        if root is None:
            return [0, True]
        left = self.balance(root.left)
        right = self.balance(root.right)
        bal_val = abs(left[0] - right[0])
        bal_max = max(left[0], right[0])
        bal_bool = left[1] and right[1] and bal_val <= 1
        return [bal_max + 1, bal_bool]

    def isBalanced(self, root: TreeNode) -> bool:
        val = self.balance(root)
        return val[1]

