"""
Linked List Random Node
https://leetcode.com/problems/linked-list-random-node/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.__head = head


    # Proof of Reservoir Sampling:
    # https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        reservoir = -1
        curr, n = self.__head, 0
        while curr:
            reservoir = curr.val if randint(1, n+1) == 1 else reservoir
            curr, n = curr.next, n+1
        return reservoir


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()