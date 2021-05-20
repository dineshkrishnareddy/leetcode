"""
Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        def dfs(root, depth):
            if not root: return
            if len(ans) == depth: ans.append([])
            ans[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return ans
