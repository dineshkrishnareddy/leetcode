"""
Boats to Save People
https://leetcode.com/problems/boats-to-save-people/
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start, end = 0, len(people) - 1
        result = 0
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            result += 1
        return result
