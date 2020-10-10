"""
Serialize and Deserialize BST
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.lst = []

        def dfs(root):
            if root is None:
                return
            self.lst.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(map(str, self.lst))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        lst = [int(x) for x in data.split(',')]

        def rec(lst, lower, upper):
            if len(lst) == 0: return None
            if not (lower < lst[0] < upper): return None

            curr = lst.pop(0)
            root = TreeNode(curr)
            root.left = rec(lst, lower, root.val)
            root.right = rec(lst, root.val, upper)
            return root

        return rec(lst, -float('inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
