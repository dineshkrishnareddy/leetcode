"""
Bag of Tokens
https://leetcode.com/problems/bag-of-tokens/
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        low,high = 0, len(tokens)-1
        result, points = 0, 0
        if len(tokens) == 0 or P < tokens[0]:
            return result

        while low <= high:
            if P >= tokens[low]:
                points += 1
                result = max(result, points)
                P -= tokens[low]
                low += 1
            elif result > 0:
                points -= 1
                P += tokens[high]
                high -= 1
            else:
                return result
        return result


tokens = [100]
P = 50
print(Solution().bagOfTokensScore(tokens, P))
tokens = [100,200,300,400]
P = 200
print(Solution().bagOfTokensScore(tokens, P))
tokens = [100,200]
P = 150
print(Solution().bagOfTokensScore(tokens, P))
tokens = [100]
P = 100
print(Solution().bagOfTokensScore(tokens, P))