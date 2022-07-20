class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = []
        for word in words:
            if self.isSubsequence(word, s):
                result.append(word)
        return len(result)

    # Taken from Problem 392 Solution
    @lru_cache
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        index = 0
        for j in range(len(t)):
            if s[index] == t[j]:
                index += 1
            if index == len(s):
                return True
        return False
