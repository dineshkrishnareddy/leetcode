class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def isInterleaveHelper(i,j,k):
            if i==-1 and j==-1 and k==-1 :
                return True
            if (i == -1 and j == -1) and k>=0:
                return False
            match1 = False
            if i>=0 and k>=0 and s3[k] == s1[i]:
                match1 = isInterleaveHelper(i-1,j,k-1)
            match2 = False
            if j>=0 and k>=0 and s3[k] == s2[j]:
                match2 = isInterleaveHelper(i,j-1,k-1)
            return (match1 or match2)
        return isInterleaveHelper(len(s1)-1,len(s2)-1,len(s3)-1)