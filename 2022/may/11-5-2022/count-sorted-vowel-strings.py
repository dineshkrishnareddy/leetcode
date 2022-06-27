class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = []
        buffer = []

        def dfs(index):
            if len(buffer) > n:
                return
            if len(buffer) == n:
                result.append(''.join(buffer[:]))

            for i, val in enumerate(vowels[index:]):
                buffer.append(val)
                dfs(index+i)
                buffer.pop()

        dfs(0)
        return len(result)

print(Solution().countVowelStrings(33))