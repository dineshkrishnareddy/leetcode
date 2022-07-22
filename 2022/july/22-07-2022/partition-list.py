# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x: int):
        if head is None:
            return None
        prev, curr = None, head
        less_nodes_head = less_nodes_tail = ListNode(0)
        more_nodes_head = more_nodes_tail = ListNode(0)
        while curr:
            if curr.val < x:
                less_nodes_tail.next = curr
                less_nodes_tail = curr
                # less_nodes_tail.next = None
            else:
                more_nodes_tail.next = curr
                more_nodes_tail = curr
                # more_nodes_tail.next = None
            curr = curr.next
        less_nodes_tail.next = None
        more_nodes_tail.next = None
        if less_nodes_head == less_nodes_tail:
            return more_nodes_head.next

        if more_nodes_head == more_nodes_tail:
            return less_nodes_head.next

        less_nodes_tail.next = more_nodes_head.next
        return less_nodes_head.next


t = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print(Solution().partition(t, 3))
