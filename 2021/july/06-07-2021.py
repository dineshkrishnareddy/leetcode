"""
1338. Reduce Array Size to The Half
https://leetcode.com/problems/reduce-array-size-to-the-half/
"""
from collections import Counter


class Solution:
    def minSetSize(self, arr) -> int:
        length = len(arr)
        counter = Counter(arr)
        vals = [(key, val) for key, val in counter.items()]
        vals.sort(key=lambda x: -x[1])
        result = 0
        removed_count = 0
        for val in vals:
            removed_count += val[1]
            result += 1
            if removed_count >= length//2:
                break
        return result


print(Solution().minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))
