"""
Recover Binary Search Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes = []

        def dfs(node):
            if node is None: return

            dfs(node.left)
            self.nodes.append(node)
            dfs(node.right)

        dfs(root)

        sorted_nodes = sorted(n.val for n in self.nodes)

        for i in range(len(sorted_nodes)):
            self.nodes[i].val = sorted_nodes[i]
