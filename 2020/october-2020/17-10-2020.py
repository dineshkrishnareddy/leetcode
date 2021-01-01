"""
Repeated DNA Sequences
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length < 10:
            return []
        unique = {}

        start = 0
        while start <= length - 10:
            unique[s[start: start + 10]] = unique.get(s[start: start + 10], 0) + 1
            start += 1

        return [x for x in unique.keys() if unique[x] > 1]
