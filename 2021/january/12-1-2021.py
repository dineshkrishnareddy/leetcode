"""
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy_head = ListNode(0)
        dummy_tail = dummy_head
        carry = 0
        while l1 and l2:
            count = l1.val + l2.val + carry
            val = count % 10
            carry = count // 10
            dummy_tail.next = ListNode(val)
            dummy_tail = dummy_tail.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            count = l1.val + carry
            val = count % 10
            carry = count // 10
            dummy_tail.next = ListNode(val)
            dummy_tail = dummy_tail.next
            l1 = l1.next

        while l2:
            count = l2.val + carry
            val = count % 10
            carry = count // 10
            dummy_tail.next = ListNode(val)
            dummy_tail = dummy_tail.next
            l2 = l2.next

        if carry:
            dummy_tail.next = ListNode(carry)
            dummy_tail = dummy_tail.next

        return dummy_head.next
