"""
Flip Binary Tree To Match Preorder Traversal
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
"""
import bisect


class Solution:
    # Dynamic Programming with Binary Search
    # Time complexity : O(nlogn). Sorting and binary search both take nlogn time.
    # Space complexity : O(n). dp array of size n is used.
    def maxEnvelopes(self, envelopes):
        # For each envelope, sorted by envelope[0] first, so envelope[1] is the the longest
        # increasing sequence(LIS) problem. When envelope[0] tie, we reverse sort by envelope[1]
        # because bigger envelope[1] can't contain the previous one.
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        # dp keeps some of the visited element in a sorted list, and its size is length Of LIS
        # sofar. It always keeps the our best chance to build a LIS in the future.
        dp = []
        for envelope in envelopes:
            i = bisect.bisect_left(dp, envelope[1])
            if i == len(dp):
                # If envelope[1] is the biggest, we should add it into the end of dp.
                dp.append(envelope[1])
            else:
                # If envelope[1] is not the biggest, we should keep it in dp and replace the
                # previous envelope[1] in this position. Because even if envelope[1] can't build
                # longer LIS directly, it can help build a smaller dp, and we will have the best
                # chance to build a LIS in the future. All elements before this position will be
                # the best(smallest) LIS sor far.
                dp[i] = envelope[1]
        # dp doesn't keep LIS, and only keep the length Of LIS.
        return len(dp)


print(Solution().maxEnvelopes([[5,4],[6,5],[6,7],[2,3]]))
