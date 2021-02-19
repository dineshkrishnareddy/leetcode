"""
Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for index, char in enumerate(s):
            if char == '(':
                stack.append([char, index])
            elif char == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append([char, index])

        result = list(s)
        while stack:
            result.pop(stack[-1][1])
            stack.pop()

        return ''.join(result)
