class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        last = None
        res = 0
        for curr in s:
            if last and values[curr] > values[last]:
                res -= 2 * values[last]
            res += values[curr]
            last = curr
        return res
