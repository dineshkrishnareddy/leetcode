"""
Remove Duplicate Letters
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0:
            return ''
        last_index = [-1] * 26
        for index in range(len(s)):
            last_index[ord(s[index]) - ord('a')] = index
        seen = [False] * 26

        res = []
        for index in range(len(s)):
            if seen[ord(s[index]) - ord('a')]:
                continue
            while len(res) != 0 and res[-1] > s[index] and index < last_index[ord(res[-1]) - ord('a')]:
                seen[ord(res[-1]) - ord('a')] = False
                res.pop()
            seen[ord(s[index]) - ord('a')] = True
            res.append(s[index])
        print(res)
        return ''.join(res)


#Solution().removeDuplicateLetters('bcabc')
Solution().removeDuplicateLetters('cbacdcbc')
