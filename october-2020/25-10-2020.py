"""
Stone Game IV
https://leetcode.com/problems/stone-game-iv/
"""


class Solution:
    def __init__(self):
        self.dp = {}

    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        if n in self.dp:
            return self.dp[n]
        winner = False
        i = 1
        while i * i <= n:
            if not self.winnerSquareGame(n - (i * i)):
                winner = True
                break
            i += 1
        self.dp[n] = winner
        return winner
