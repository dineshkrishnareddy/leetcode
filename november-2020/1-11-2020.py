"""
Convert Binary Number in a Linked List to Integer
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return 0

        result = 0
        while head is not None:
            result = result << 1
            if head.val:
                result = result | 1
            head = head.next

        return result
