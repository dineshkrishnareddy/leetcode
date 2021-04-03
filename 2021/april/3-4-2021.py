"""
Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/
"""


class Solution:
    def longestValidParentheses(self, S: str) -> int:
        stack, ans = [-1], 0
        for i in range(len(S)):
            if S[i] == '(': stack.append(i)
            elif len(stack) == 1: stack[0] = i
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return ans


print(Solution().longestValidParentheses('())((()))'))
