"""
Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
"""


class Solution:
    def numPairsDivisibleBy60(self, time):
        length = len(time)
        if length == 0:
            return 0
        unique = {}
        count = 0
        for index, val in enumerate(time):
            key = val%60
            if key in unique:
                unique[key].append(index)
            else:
                unique[key] = [index]
        print(unique)

        for index, val in enumerate(time):
            key = (60-val)%60
            if key in unique:
                count += len(unique[key])
                if index in unique[key]:
                    count -= 1
        return count//2


print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
print(Solution().numPairsDivisibleBy60([60, 60, 60]))
