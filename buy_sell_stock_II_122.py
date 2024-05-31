from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        profit = 0
        i = 0
        while i < len(prices):
            profit = max(profit, prices[i] - min_price)
            if prices[i - 1] > prices[i]:
                max_profit += profit
                profit = 0
                min_price = prices[i]
            i += 1

        return max_profit + profit
