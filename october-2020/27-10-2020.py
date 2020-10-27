"""
Linked List Cycle II
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getCycleStart(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        cycle_start = self.getCycleStart(head)

        if cycle_start is None:
            return None

        while head != cycle_start:
            head = head.next
            cycle_start = cycle_start.next

        return head