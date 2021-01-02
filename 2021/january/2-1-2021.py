"""
Find a Corresponding Node of a Binary Tree in a Clone of That Tree
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_node(self, original, cloned, target):
        if original is None:
            return None
        if original == target:
            return cloned

        return self.get_node(original.left, cloned.left, target) or self.get_node(original.right, cloned.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.get_node(original, cloned, target)
