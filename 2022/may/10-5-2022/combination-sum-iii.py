class Solution:
    def combinationSum3(self, k, n):
        result = []
        items = []

        def dfs(count, index):
            if len(items) > k:
                return
            
            if count == n and len(items) == k:
                result.append(items[:])
                return
            
            for i in range(index, 10):
                items.append(i)
                dfs(count+i, i+1)
                items.pop()

        dfs(0, 1)
        return result

print(Solution().combinationSum3(3, 7))