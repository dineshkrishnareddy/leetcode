class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp=[nums[0]]+[0]*(len(nums)-1)
        for i in range(1,len(nums)): dp[i]=nums[i]+max(dp[max(0,i-k):i])
        return dp[-1]

    def maxResult1(self, nums: List[int], k: int) -> int:
        heap=[(0,-k)]
        for i in range(len(nums)):
            while i-heap[0][1]>k: heappop(heap)
            nums[i]-=heap[0][0]
            heappush(heap,(-nums[i],i))
        return nums[-1]