"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""


class Solution:
    def trap(self, height) -> int:
        n=len(height)
        l=0
        r=n-1
        lmax=0
        rmax=0
        ans=0
        while l<=r:
            if height[l]<=height[r]:
                if height[l]>=lmax:
                    lmax=height[l]
                else:
                    ans+=lmax-height[l]
                l+=1
            else:
                if height[r]>=rmax:
                    rmax=height[r]
                else:
                    ans+=rmax-height[r]
                r-=1
        return ans


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
