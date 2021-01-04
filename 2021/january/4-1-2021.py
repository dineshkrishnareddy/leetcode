"""
Merge Two Sorted Lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy_head = ListNode(0)
        dummy_tail = dummy_head

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                dummy_tail.next = l1
                l1 = l1.next
            else:
                dummy_tail.next = l2
                l2 = l2.next
            dummy_tail = dummy_tail.next

        if l1 is not None:
            while l1 is not None:
                dummy_tail.next = l1
                l1 = l1.next
                dummy_tail = dummy_tail.next

        if l2 is not None:
            while l2 is not None:
                dummy_tail.next = l2
                l2 = l2.next
                dummy_tail = dummy_tail.next

        return dummy_head.next
