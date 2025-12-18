'''
https://leetcode.com/problems/coin-change/description/
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''


'''
top down:


'''
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxval = 999999
        @cache
        def change_for_amount_with_least_coins(amount_left):
            if amount_left < 0:
                return maxval
            if amount_left == 0:
                return 0
            prevMin = maxval
            for coin in coins:
                prevMin = min(prevMin, (change_for_amount_with_least_coins(amount_left - coin)) + 1)
            return prevMin


        
        val = change_for_amount_with_least_coins(amount)
        if val == maxval:
            return -1
        return val
