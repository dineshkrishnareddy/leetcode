"""
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def traverse(root, maxi):
            nonlocal count
            if root is None:
                return
            if root.val >= maxi:
                count += 1
            maxi = max(maxi, root.val)
            traverse(root.left, maxi)
            traverse(root.right, maxi)

        traverse(root, float('-inf'))
        return count
