"""
Rotate List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k < 1:
            return head

        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        k = (count - k) % count

        if k == 0:
            return head

        tail1 = head1 = head
        while k:
            tail1 = head1
            head1 = head1.next
            k -= 1

        head2 = head1
        while head1.next is not None:
            head1 = head1.next

        tail1.next = None
        head1.next = head

        return head2
