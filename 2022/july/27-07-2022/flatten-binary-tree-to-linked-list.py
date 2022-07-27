class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node: return
            if node.left:
                next = node.left
                while next.right:
                    next = next.right
                next.right = node.right
                node.right = node.left
                node.left = None
            traverse(node.right)
        traverse(root)
