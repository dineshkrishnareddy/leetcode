"""
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def get_path(root, val, path):
            if root is None:
                return False, []
            path.append(root)
            if root == val:
                return True, path
            present_left, l = get_path(root.left, val, path)
            if present_left:
                return True, l
            present_right, r = get_path(root.right, val, path)
            if present_right:
                return True, r
            path.pop()
            return False, []
        _, p_path = get_path(root, p, [])
        _, q_path = get_path(root, q, [])
        for idx in range(len(p_path)):
            print(p_path[idx].val)
        for idx in range(len(q_path)):
            print(q_path[idx].val)
        result = None
        while p_path and q_path and p_path[0] == q_path[0]:
            result = p_path.pop(0)
            q_path.pop(0)
        return result
