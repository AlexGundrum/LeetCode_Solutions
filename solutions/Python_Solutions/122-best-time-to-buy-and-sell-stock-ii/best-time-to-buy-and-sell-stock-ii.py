'''
lpan

i can only have one share at any time. 
i can sell and buy back stock multiple times in same day. when would i want to do this? 
that'd be equivalent to holding im ps. 

min profit is 0 bucks doing nothing. 


ok so for ith day, 


'''
from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LEN = len(prices)

        @lru_cache(maxsize=1280)
        def dp(day, holdingStock):
            #options:
            if day >= LEN:
                return 0
            
            #skip, just hold. 
            skip = dp(day + 1, holdingStock)

            sell = 0

            if holdingStock:
                #we bought a stock. sell it and move forward
                sell = dp(day + 1, False) + prices[day]
            
            buy = 0
            if not holdingStock:
                buy = dp(day + 1, True) - prices[day]
            
            return max(skip, sell, buy)
                
            

        return dp(0, False)