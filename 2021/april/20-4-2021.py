"""
N-ary Tree Preorder Traversal
"""

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.vals = []

    def traverse(self, root):
        if root is None:
            return
        self.vals.append(root.val)

        for child in root.children:
            self.traverse(child)

    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        self.traverse(root)
        return self.vals
