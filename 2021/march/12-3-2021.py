"""
Coin Change
https://leetcode.com/problems/coin-change/
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        got = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k


print(Solution().hasAllCodes("00110110", 2))
