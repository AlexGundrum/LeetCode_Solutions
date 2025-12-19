'''
can complete at most two transactions? each day? 
im not even sure what this means. just means you must sell before you buy????
LOL we can sell twice. ok.

'''

from functools import lru_cache 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LEN = len(prices)

        @lru_cache(maxsize=512)
        def dp(day, holding_stock, sales_left):
            if day >= LEN:
                return 0
            
            if sales_left <= 0:
                return 0
            
            #continue without doing anything:
            hold = dp(day + 1, holding_stock, sales_left)
            buy, sell = 0, 0

            if not holding_stock:
                #we buy at this value
                buy = -prices[day] + dp(day + 1, True, sales_left)
            
            if holding_stock: 
                #sell at this value
                sell = prices[day] + dp(day + 1, False, sales_left - 1)
            
            return max(buy, sell, hold)
        
        return dp(0, False, 2)