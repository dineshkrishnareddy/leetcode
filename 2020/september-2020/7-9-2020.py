"""
https://leetcode.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        length_pattern = len(pattern)
        length_string = len(string)
        if length_pattern == 0 or length_string == 0:
            return False
        string_split = string.split(' ')
        visited = {}
        if length_pattern != len(string_split):
            return False
        for index, char in enumerate(pattern):
            if char not in visited:
                if string_split[index] in visited.values():
                    return False
                visited[char] = string_split[index]
            elif visited[char] != string_split[index]:
                return False
        return True
