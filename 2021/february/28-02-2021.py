"""
Score of Parentheses
https://leetcode.com/problems/score-of-parentheses/
"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for char in S:
            if char == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)

        return stack.pop()


# string = "()"
# print(Solution().scoreOfParentheses(string))
# string = "(())"
# print(Solution().scoreOfParentheses(string))
string = "((()))"
print(Solution().scoreOfParentheses(string))
# string = "((()()))"
# print(Solution().scoreOfParentheses(string))
# string = "((())"
# print(Solution().scoreOfParentheses(string))
