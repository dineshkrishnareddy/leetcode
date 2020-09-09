"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # v1_split = version1.split('.')
        # v2_split = version2.split('.')
        # curr = 0
        # end = max(len(v1_split), len(v2_split))
        # while curr <= end:
        #     try:
        #         v1_curr_val = int(v1_split[curr])
        #     except:
        #         v1_curr_val = 0
        #     try:
        #         v2_curr_val = int(v2_split[curr])
        #     except:
        #         v2_curr_val = 0
        #     if v1_curr_val > v2_curr_val:
        #         return 1
        #     elif v1_curr_val < v2_curr_val:
        #         return -1
        #     curr += 1
        # return 0
        v1_split = version1.split('.')
        v2_split = version2.split('.')
        curr = 0
        end = max(len(v1_split), len(v2_split))
        while curr <= end:
            v1_curr_val = int(v1_split[curr]) if curr < len(v1_split) else 0
            v2_curr_val = int(v2_split[curr]) if curr < len(v2_split) else 0
            if v1_curr_val != v2_curr_val:
                return 1 if v1_curr_val > v2_curr_val else -1
            curr += 1
        return 0

print(Solution().compareVersion("1.0.1", "1.0"))
print(Solution().compareVersion("1.0.1", "1"))
print(Solution().compareVersion("7.5.2.4", "7.5.3"))
print(Solution().compareVersion("0.1", "1.1"))
