"""
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next

        def reverse(root):
            ans = None
            while root:
                nxt = root.next
                root.next = ans
                ans = root
                root = nxt
            return ans

        head2 = reverse(slow)
        head1 = head
        while head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True
