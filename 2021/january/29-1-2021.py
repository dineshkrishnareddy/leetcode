"""
Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)

        def dfs(curr, x, y):
            if curr:
                d[x].append((y, curr.val))
                dfs(curr.left, x - 1, y + 1)
                dfs(curr.right, x + 1, y + 1)

        dfs(root, 0, 0)
        return [[v[1] for v in sorted(d[k])] for k in sorted(d)]
