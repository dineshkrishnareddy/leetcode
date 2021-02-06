"""
Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.level_node_values = defaultdict(list)

    def parse(self, root, level):
        if not root:
            return
        self.level_node_values[level].append(root.val)
        self.parse(root.left, level + 1)
        self.parse(root.right, level + 1)

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.parse(root, 0)
        result = []
        for key in sorted(self.level_node_values):
            result.append(self.level_node_values[key][-1])
        return result
