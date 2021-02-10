"""
Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
"""

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        new_head = head
        dummy_head = Node(0)
        dummy_tail = dummy_head
        mapping = {}
        while new_head:
            node = Node(new_head.val)
            dummy_tail.next = node
            mapping[new_head] = node
            new_head = new_head.next
            dummy_tail = dummy_tail.next

        new_head = head
        dummy_tail = dummy_head.next
        while new_head:
            dummy_tail.random = mapping.get(new_head.random, None)
            new_head = new_head.next
            dummy_tail = dummy_tail.next

        return dummy_head.next
