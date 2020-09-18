"""
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        length = len(prices)
        if length == 0:
            return result
        curr_min, curr_max = prices[0], prices[0]
        for price in prices[1:]:
            if price < curr_min:
                result = max(result, curr_max-curr_min)
                curr_min = price
                curr_max = price
            curr_max = max(curr_max, price)
        result = max(result, curr_max-curr_min)
        return result
