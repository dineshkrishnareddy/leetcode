"""
https://leetcode.com/problems/delete-node-in-a-bst/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_successor_val(self, root):
        root = root.right
        while root.left is not None:
            root = root.left
        return root.val

    def inorder_predecessor_val(self, root):
        root = root.left
        while root.right is not None:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is not None:
                root.val = self.inorder_predecessor_val(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.inorder_successor_val(root)
                root.right = self.deleteNode(root.right, root.val)
        return root
