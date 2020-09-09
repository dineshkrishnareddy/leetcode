"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def get_sum(self, root, path):
        path.append(str(root.val))
        if root.left is None and root.right is None:
            val = int(''.join(path), 2)
            self.sum += val
            path.pop()
            return

        if root.left is not None:
            self.get_sum(root.left, path)
        if root.right is not None:
            self.get_sum(root.right, path)
        path.pop()

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return self.sum
        self.get_sum(root, [])
        return self.sum
