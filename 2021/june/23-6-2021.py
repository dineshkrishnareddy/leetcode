"""
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head == None:
            return None

        dummy = ListNode(0, head)
        prev, curr = dummy, dummy.next
        k = 1
        while k < left:
            prev, curr = curr, curr.next
            k += 1
        non_cycle_start, non_cycle_end = prev, curr
        while curr and k <= right:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
            k += 1
        non_cycle_start.next = prev
        non_cycle_end.next = curr
        return dummy.next
