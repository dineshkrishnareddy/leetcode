"""
Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def dfs(head, tail):
            if head == tail: return None
            fast, slow = head, head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return TreeNode(slow.val, dfs(head, slow), dfs(slow.next, tail))

        return dfs(head, None)
