"""
House Robber III
https://leetcode.com/problems/house-robber-iii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def decision(node: TreeNode) -> list:
            if not node: return [0, 0]

            [leftRob, leftNot] = decision(node.left)
            [rightRob, rightNot] = decision(node.right)

            rob = node.val + leftNot + rightNot
            notRob = max(leftRob + rightRob, leftRob + rightNot, leftNot + rightRob, leftNot + rightNot)

            return [rob, notRob]

        result = decision(root)
        return max(result)
