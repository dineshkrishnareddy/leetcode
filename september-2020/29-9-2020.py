"""
Word Break
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        length = len(s)

        #         def dfs(start, length):
        #             if start >= length:
        #                 return True

        #             for index in range(start, length):
        #                 if s[start:index+1] in words:
        #                     if dfs(index+1, length):
        #                         return True
        #             return False
        #         return dfs(0, length)
        dp = [False for _ in range(length + 1)]
        dp[0] = True
        for start in range(length):
            if not dp[start]:
                continue
            for end in range(start + 1, length + 1):
                if s[start:end] in words:
                    dp[end] = True
        return dp[-1]
