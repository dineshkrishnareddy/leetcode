"""
Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        push_size = len(pushed)
        pop_size = len(popped)
        i, j = 0, 0

        if push_size != pop_size:
            return False

        while i < push_size:
            while i < push_size and pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            if i < push_size:
                stack.append(pushed[i])
                i += 1
            while j < pop_size and len(stack) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return len(stack) == 0
