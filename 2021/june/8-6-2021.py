"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0, 0, len(inorder), preorder, inorder)

    def helper(self, preindex, instart, inend, preorder, inorder):
        if preindex > len(preorder) - 1 or instart > inend:
            return None

        index = inorder.index(preorder[preindex])
        return TreeNode(
            val=preorder[preindex],
            left=self.helper(preindex + 1, instart, index - 1, preorder, inorder),
            right=self.helper(preindex + index - instart + 1, index + 1, inend, preorder, inorder),
        )
