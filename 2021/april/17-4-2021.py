"""
Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""


class Solution:
    def removeDuplicates1(self, S: str, K: int) -> str:
        count, i = 1, 1
        while i < len(S):
            if S[i] == S[i - 1]:
                count += 1
            else:
                count = 1
            if count == K: S = self.removeDuplicates(S[:i - K + 1] + S[i + 1:], K)
            i += 1
        return S

    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st, i, j = list(S), [0], 1, 1
        while j < len(S):
            SC[i] = SC[j]
            if i == 0 or SC[i] != SC[i - 1]:
                st.append(i)
            elif i - st[-1] + 1 == K:
                i = st.pop() - 1
            i += 1
            j += 1
        return "".join(SC[:i])


print(Solution().removeDuplicates('deeedbbcccbdaa', 3))
