"""
Integer to Roman
https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = ''

        for i, v in enumerate(vals):
            res += (num // v) * romans[i]
            num %= v

        return res


print(Solution().intToRoman(58))
