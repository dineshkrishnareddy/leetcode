"""
473. Matchsticks to Square
https://leetcode.com/problems/matchsticks-to-square/
"""


class Solution:
    def makesquare(self, matchsticks) -> bool:
        length = len(matchsticks)
        total_len = sum(matchsticks)
        max_side_len = sum(matchsticks) // 4
        if total_len % 4 != 0:
            return False
        sums = [0 for _ in range(4)]
        matchsticks.sort(reverse=True)

        def match(index):
            if index == length:
                return (sums[0] == sums[1] == sums[2] == sums[3])

            for i in range(4):
                if sums[i] + matchsticks[index] <= max_side_len:
                    sums[i] += matchsticks[index]
                    if match(index + 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False

        return match(0)


print(Solution().makesquare([1,1,2,2,2]))
print(Solution().makesquare([3,3,3,3,4]))
