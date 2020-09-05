#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.elements = []

    def travelTree(self, root):
        if root is None:
            return
        self.elements.append(root.val)
        self.travelTree(root.left)
        self.travelTree(root.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.travelTree(root1)
        self.travelTree(root2)
        return sorted(self.elements)
