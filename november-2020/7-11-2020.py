"""
Add Two Numbers II
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodes_to_stack(self, node):
        stack = []

        while node is not None:
            stack.append(node)
            node = node.next

        return stack

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        stack_l1 = self.nodes_to_stack(l1)
        stack_l2 = self.nodes_to_stack(l2)

        result = None
        carry = 0
        while len(stack_l1) and len(stack_l2):
            n1, n2 = stack_l1.pop(), stack_l2.pop()
            addition = n1.val + n2.val + carry
            carry = int(addition / 10)
            val = addition % 10
            result = ListNode(val, result)

        if len(stack_l1):
            while len(stack_l1):
                n1 = stack_l1.pop()
                addition = n1.val + carry
                carry = int(addition / 10)
                val = addition % 10
                result = ListNode(val, result)
        else:
            while len(stack_l2):
                n1 = stack_l2.pop()
                addition = n1.val + carry
                carry = int(addition / 10)
                val = addition % 10
                result = ListNode(val, result)
        if carry:
            result = ListNode(carry, result)

        return result
