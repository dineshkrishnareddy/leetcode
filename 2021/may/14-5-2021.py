"""
Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None

        def traverse(root):
            nonlocal prev
            if root is None:
                return None
            traverse(root.right)
            traverse(root.left)
            root.right = prev
            root.left = None
            prev = root

        traverse(root)
