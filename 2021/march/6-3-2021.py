"""
Short Encoding of Words
https://leetcode.com/problems/short-encoding-of-words/
"""


class Solution:
    def minimumLengthEncoding(self, words) -> int:
        trie = {}
        for word in words:
            node = trie
            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {}
                node = node[ch]

        if not trie: return 0

        def dfs(node=trie, curlvl=1):
            if not node: return curlvl
            return sum([dfs(child, curlvl+1) for child in node.values()])

        return dfs()


# print(Solution().minimumLengthEncoding(['t', 'the']))
print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
