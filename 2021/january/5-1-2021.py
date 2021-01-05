"""
Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        dummy_head = ListNode(0)
        dummy_tail = dummy_head

        while head:
            curr_val = head.val
            count = 0
            while head and head.val == curr_val:
                prev = head
                head = head.next
                count += 1
            if count == 1:
                dummy_tail.next = prev
                dummy_tail = dummy_tail.next
                dummy_tail.next = None
        return dummy_head.next
