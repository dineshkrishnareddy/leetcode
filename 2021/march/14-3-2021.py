"""
Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        buffer, cur = [], head

        while cur:
            buffer.append(cur)
            cur = cur.next

        buffer[k - 1].val, buffer[-k].val = buffer[-k].val, buffer[k - 1].val

        return buffer[0]
