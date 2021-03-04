"""
Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        unique = {}
        result = None

        while headA:
            unique[headA] = True
            headA = headA.next

        while headB:
            if headB in unique:
                return headB
            headB = headB.next

        return result

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
