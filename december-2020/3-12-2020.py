"""
Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        dummy = curr = TreeNode()
        stack = []

        while stack or root:

            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            curr.right = root

            curr = curr.right
            root = root.right

            curr.left = None

        return dummy.right

