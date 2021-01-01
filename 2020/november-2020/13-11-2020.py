"""
Populating Next Right Pointers in Each Node
"""

"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = [root, None]

        while len(queue):
            curr = queue.pop(0)
            if curr is None and len(queue) == 0:
                return root
            elif curr is None:
                queue.append(None)
                continue
            else:
                curr.next = queue[0]
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        return root


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
Solution().connect(root)

