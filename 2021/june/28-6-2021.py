"""
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for char in s:
            if result and result[-1] == char:
                result.pop()
            else:
                result.append(char)
        return ''.join(result)
