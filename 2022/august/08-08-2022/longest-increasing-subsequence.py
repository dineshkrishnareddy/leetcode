class Solution:
    def lengthOfLIS(self, nums):
        length = len(nums)
        dp = [0] * (length+1)
        for i in range(length):
            curr_max = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_max = max(curr_max, dp[j])
            dp[i] = curr_max+1
        return max(dp)


print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
