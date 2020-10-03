"""
Combination Sum
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for c in candidates:
            for i in range(target + 1):
                if i < c:
                    continue
                elif i == c:
                    dp[i].append([c])
                else:
                    for blist in dp[i - c]:
                        dp[i].append(blist + [c])
        return dp[target]
