"""
Partition List
https://leetcode.com/problems/partition-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = small_tail = ListNode(0)
        big_head = big_tail = ListNode(0)

        while head:
            if head.val < x:
                small_tail.next = ListNode(head.val)
                small_tail = small_tail.next
            else:
                big_tail.next = ListNode(head.val)
                big_tail = big_tail.next
            head = head.next

        small_tail.next = big_head.next
        return small_head.next

