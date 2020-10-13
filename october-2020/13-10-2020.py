"""
Sort List
https://leetcode.com/problems/sort-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = fast = head

        while fast is not None and fast.next is not None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        left_side = self.sortList(head)
        right_side = self.sortList(slow)

        return self.mergeLists(left_side, right_side)

    def mergeLists(self, left_head, right_head):
        curr_head = curr_tail = ListNode(0)
        while left_head is not None and right_head is not None:
            if left_head.val < right_head.val:
                curr_tail.next = ListNode(left_head.val)
                left_head = left_head.next
            else:
                curr_tail.next = ListNode(right_head.val)
                right_head = right_head.next
            curr_tail = curr_tail.next

        while left_head is not None:
            curr_tail.next = ListNode(left_head.val)
            left_head = left_head.next
            curr_tail = curr_tail.next

        while right_head is not None:
            curr_tail.next = ListNode(right_head.val)
            right_head = right_head.next
            curr_tail = curr_tail.next

        return curr_head.next
