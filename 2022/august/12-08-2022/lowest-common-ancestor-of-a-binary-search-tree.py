# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', prev=None) -> 'TreeNode':
        # return self.visit(root, root, p, q)
        if p.val == root.val or q.val == root.val:
            return prev
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q, root)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q, root)
        else:
            return root
