"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ['()']
        result = []

        def backtracking(sequence, open_count, close_count):
            if open_count == close_count == n:
                result.append(''.join(sequence))
                return

            if open_count < n:
                sequence.append('(')
                backtracking(sequence, open_count + 1, close_count)
                sequence.pop()

            if close_count < open_count:
                sequence.append(')')
                backtracking(sequence, open_count, close_count + 1)
                sequence.pop()
            return

        backtracking([], 0, 0)
        return result


print(Solution().generateParenthesis(8))
