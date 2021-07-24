"""
814. Binary Tree Pruning
https://leetcode.com/problems/binary-tree-pruning/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        def traverse(root):
            if root is None:
                return None

            root.left = traverse(root.left)
            root.right = traverse(root.right)

            if root.left is None and root.right is None and root.val == 0:
                return None

            return root

        return traverse(root)
