class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node=root, level=1):
            if not node: return

            if len(ans) < level:
                ans.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

            return

        dfs()
        return ans
