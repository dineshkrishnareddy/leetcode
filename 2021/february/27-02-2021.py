"""
Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d, div, count = abs(dividend), abs(divisor), 0
        while d >= div:
            d = d-div
            count += 1
        return -count if (dividend < 0 or divisor < 0) and (not (dividend < 0 and divisor < 0)) else count

    def divide1(self, dividend: int, divisor: int) -> int:
        d, div, count = abs(dividend), abs(divisor), 0

        def check(d, div):
            i, count, c = 0, 0, 0
            while d >= div:
                if i == 0:
                    count = 1
                d -= div
                div += div
                if i != 0:
                    count += count
                c += count
                i += 1
            return d, c

        while d >= abs(divisor):
            d, c = check(d, div)
            print(d, c)
            count += c
        if dividend < 0 or divisor < 0:
            if not (dividend < 0 and divisor < 0):
                sign = count + count
                count = count - sign

        if -(2) ** 31 > count or count > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return count


print(Solution().divide(-1, -1))
