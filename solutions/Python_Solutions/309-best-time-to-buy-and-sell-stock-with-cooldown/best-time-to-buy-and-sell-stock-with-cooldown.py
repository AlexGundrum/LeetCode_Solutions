from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LEN = len(prices)
        
        @lru_cache(maxsize=None)
        def dp(day, holding_stock):
            if day >= LEN:
                return 0
            
            hold = dp(day + 1, holding_stock)

            sell, buy = 0, 0

            if not holding_stock:
                buy = -prices[day] + dp(day + 1, True)
            
            if holding_stock:
                sell = prices[day] + dp(day + 2, False)

            return max(buy, sell, hold)

        return dp(0, False)