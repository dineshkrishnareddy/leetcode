"""
Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            last_digit = int(n % 10)
            if last_digit:
                result += 1
            n = n // 10
        return result


print(Solution().hammingWeight(int('00000000000000000000000000001011')))
print(Solution().hammingWeight(11111111111111111111111111111101))
