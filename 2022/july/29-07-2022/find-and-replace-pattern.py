class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        result = []
        length = len(pattern)
        for word in words:
            tmp1 = {}
            tmp2 = {}
            if length == len(word):
                curr = 0
                while curr < length:
                    if pattern[curr] in tmp1:
                        if tmp1[pattern[curr]] != word[curr]:
                            break
                    else:
                        tmp1[pattern[curr]] = word[curr]

                    if word[curr] in tmp2:
                        if tmp2[word[curr]] != pattern[curr]:
                            break
                    else:
                        tmp2[word[curr]] = pattern[curr]
                    curr += 1
                if curr == length:
                    result.append(word)
        return result


print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
