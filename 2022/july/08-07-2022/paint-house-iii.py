class Solution:
    def minCost1(self, houses: List[int], cost: List[List[int]], R: int, C: int, target: int) -> int:
        # think as if we are traveling downward
        # at any point, if switch our column then (target--)

        @functools.cache
        def dp(x, y, k):  # O(100*20*100) time space
            if x == R:
                return 0 if k == 0 else math.inf
            elif k <= 0:
                return math.inf

            # if this house is already colored, dont recolor!!
            if houses[x] > 0 and houses[x] != y + 1: return math.inf

            cur_cost = 0 if houses[x] == y + 1 else cost[x][y]

            # now try all columns! O(20) time
            res = math.inf
            for c in range(C):
                if c == y:
                    res = min(res, cur_cost + dp(x + 1, c, k))
                else:
                    res = min(res, cur_cost + dp(x + 1, c, k - 1))
            # print('dp',x,y,k,'=',res)
            return res

        ans = min(dp(0, y, target) for y in range(C))

        return -1 if ans == math.inf else ans
