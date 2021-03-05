"""
Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return None

        levels = defaultdict(list)

        def traverse(root, level):
            if root is None:
                return

            levels[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 0)

        result = []
        for _, val in levels.items():
            result.append(sum(val) / len(val))
        return result
