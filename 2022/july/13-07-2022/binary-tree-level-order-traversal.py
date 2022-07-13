# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        result = []

        def helper(abc, level):
            if abc is None:
                return
            if level >= len(result):
                result.append([])
            result[level].append(abc.val)

            helper(abc.left, level+1)
            helper(abc.right, level+1)

        helper(root, 0)
        return result


tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().levelOrder(tree))
