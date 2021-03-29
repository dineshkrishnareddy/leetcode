"""
Flip Binary Tree To Match Preorder Traversal
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return [-1] if len(self.flipped) > 0 and self.flipped[0] == -1 else self.flipped
