"""
Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    opening = ['[', '(', '{']
    closing = [']', ')', '}']

    def __init__(self):
        self.map = {}
        for index, val in enumerate(self.opening):
            self.map[val] = self.closing[index]

    def isValid(self, s: str) -> bool:
        length = len(s)

        stack = []
        for char in s:
            if char in self.opening:
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                open_brace = stack.pop()
                if char != self.map[open_brace]:
                    return False
        return len(stack) == 0
