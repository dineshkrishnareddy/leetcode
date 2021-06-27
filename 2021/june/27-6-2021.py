"""
135. Candy
https://leetcode.com/problems/candy/
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        tmp = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                tmp[i] = tmp[i - 1] + 1

        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                tmp[i] = max(tmp[i + 1] + 1, tmp[i])

        return sum(tmp)
