"""
18. 4Sum
https://leetcode.com/problems/4sum/
"""


class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        if len(a)<4:
            return []
        a.sort()
        ans=[]
        for i in range(len(a)-3):
            for j in range(i+1,len(a)-2):
                l,r=j+1,len(a)-1
                while l<r:
                    p=a[i]+a[j]+a[l]+a[r]
                    if p==target:
                        ans+=[a[i],a[j],a[l],a[r]],
                        l+=1
                        r-=1
                    elif p<target:
                        l+=1
                    else:
                        r-=1
        return set(tuple(p) for p in ans)
