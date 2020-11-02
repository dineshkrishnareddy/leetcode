"""
Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        new_head, new_tail = head, head
        curr = head.next
        while curr is not None:
            temp_head = new_head
            less_than_curr = new_head
            while temp_head != curr and temp_head.val <= curr.val:
                less_than_curr = temp_head
                temp_head = temp_head.next

            if temp_head == new_head:
                new_tail.next = curr.next
                curr.next = new_head
                new_head = curr
            elif temp_head.val <= curr.val:
                new_tail = curr
            else:
                new_tail.next = curr.next
                curr.next = less_than_curr.next
                less_than_curr.next = curr
            curr = new_tail.next

        return new_head


head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print(Solution().insertionSortList(head))

# print(Solution().insertionSortList(None))