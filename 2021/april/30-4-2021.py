"""
Powerful Integers
https://leetcode.com/problems/powerful-integers/
"""


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        for i in range(bound):
            pow_x = x ** i
            if pow_x > bound:
                break
            for j in range(bound):
                pow_y = y ** j
                if pow_x + pow_y > bound:
                    break
                result.add(pow_x + pow_y)
                if y == 1: break
            if x == 1: break
        return result
