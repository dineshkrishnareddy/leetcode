# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:

        # reverse function
        def reverse(prev, head):
            if not head:
                return prev
            tmp = head.next
            head.next = prev
            return reverse(head, tmp)

        # use slow and fast pointer to get the mid of list
        sp = head
        fp = sp
        while (fp and fp.next):
            sp = sp.next
            fp = fp.next.next

        mid = reverse(None, sp)

        # check for palindrome
        def check(mid, head):
            if (not mid):
                return True
            elif (mid.val == head.val):
                return check(mid.next, head.next)
            else:
                return False

        return check(mid, head)