class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        N = len(nums)

        def findStarting():
            lo, hi = 0, N - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo if lo < len(nums) and nums[lo] == target else -1

        def findEnding():
            lo, hi = 0, N - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return hi if nums[hi] == target else -1

        return [findStarting(), findEnding()] if N > 0 else [-1, -1]
