class Solution:

    def partitionLabels(self, S: str):
        if len(S) == 0:
            return []
        chars = {}
        for index, char in enumerate(S):
            chars[char] = index
        result = []
        length = len(S)
        curr_begin, curr_end, begin = 0, 0, 0
        while curr_begin < length:
            curr_end = max(curr_end, chars[S[curr_begin]])
            if curr_begin == curr_end:
                result.append(curr_end + 1 - begin)
                begin = curr_begin+1
            curr_begin += 1
        return result

    # def partitionLabels(self, S: str):
    #     if len(S) == 0:
    #         return []
    #     chars = {}
    #     for index, char in enumerate(S):
    #         chars[char] = index
    #     result = []
    #     length = len(S)
    #     curr_begin = 0
    #     curr_end = 0
    #     while curr_begin < length:
    #         curr_end = max(curr_end, chars[S[curr_begin]])
    #         begin = curr_begin
    #         while curr_begin < curr_end:
    #             curr_end = max(curr_end, chars[S[curr_begin]])
    #             curr_begin += 1
    #         result.append(curr_end + 1 - begin)
    #         curr_begin = curr_end + 1
    #     return result

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))