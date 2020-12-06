"""
Populating Next Right Pointers in Each Node II
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.pointersInLevels = []

        def traverseTree(node, level):
            if node:
                if level < len(self.pointersInLevels):
                    self.pointersInLevels[level].next = node
                    self.pointersInLevels[level] = node
                else:
                    self.pointersInLevels.append(node)
                    node.next = None

                traverseTree(node.left, level + 1)
                traverseTree(node.right, level + 1)

        traverseTree(root, 0)

        return root
