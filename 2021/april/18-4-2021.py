"""
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = p2 = head
        temp = ListNode(0)
        while n:
            p1 = p1.next
            n -= 1
        while p1:
            temp = p2
            p1 = p1.next
            p2 = p2.next

        temp.next = p2.next
        return head if p2 != head else head.next
