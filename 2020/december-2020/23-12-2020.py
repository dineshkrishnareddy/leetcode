"""
Swap Nodes in Pairs
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        first, second = head, head.next
        dummy = ListNode()
        dummy.next = second or first
        prev = dummy
        while first and second:
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            first = first.next
            if first:
                second = first.next
        return dummy.next
