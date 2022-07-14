# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None

        inorder_index = inorder.index(preorder.pop(0))
        left = self.buildTree(preorder, inorder[:inorder_index])
        right = self.buildTree(preorder, inorder[inorder_index+1:])
        return TreeNode(
            inorder[inorder_index],
            left,
            right,
        )


# tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
