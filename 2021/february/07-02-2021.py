"""
Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/
"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        length = len(s)
        if not length:
            return []
        result = [float('inf') for _ in range(length)]
        stack = []
        for index in range(length):
            if s[index] == c:
                result[index] = 0
                count = 0
                while len(stack):
                    count += 1
                    stack_index = stack.pop()
                    result[stack_index] = min(result[stack_index], count)
            else:
                stack.append(index)

        for index in range(length - 1, -1, -1):
            if s[index] == c:
                result[index] = 0
                count = 0
                while len(stack):
                    count += 1
                    stack_index = stack.pop()
                    result[stack_index] = min(result[stack_index], count)
            else:
                stack.append(index)

        return result
