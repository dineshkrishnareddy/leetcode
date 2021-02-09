"""
Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        def postorder(root, curr_sum):
            if not root:
                return curr_sum
            curr_sum = postorder(root.right, curr_sum)
            root.val = root.val + curr_sum
            curr_sum = root.val
            curr_sum = postorder(root.left, curr_sum)
            return curr_sum

        postorder(root, 0)
        return root
