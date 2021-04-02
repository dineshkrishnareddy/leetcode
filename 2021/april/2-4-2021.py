"""
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        weights = []
        for st in strs:
            counter = Counter(st)
            weights.append((counter.get("0", 0), counter.get("1", 0)))
        self.visited = {}
        return self.recursiveWithMemo(strs, weights, len(strs) - 1, (m, n))

    def recursiveWithMemo(self, strs, weights, index, wt):
        if wt == (0, 0) or index < 0: return 0
        if (index, wt) in self.visited:
            return self.visited[(index, wt)]
        else:
            curr = weights[index]
            if curr[0] <= wt[0] and curr[1] <= wt[1]:
                self.visited[(index, wt)] = max(
                    1 + self.recursiveWithMemo(strs, weights, index - 1, (wt[0] - curr[0], wt[1] - curr[1])),
                    self.recursiveWithMemo(strs, weights, index - 1, wt)
                )
            else:
                self.visited[(index, wt)] = self.recursiveWithMemo(strs, weights, index - 1, wt)
            return self.visited[(index, wt)]


print(Solution().findMaxForm(["10","0","1"], 1, 1))
