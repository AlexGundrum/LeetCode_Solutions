'''
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
'''

'''
so we can either add our val and go two forward
or 
not add our val and go one forward

return max of these two
'''

from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        @cache
        def max_money_from_house(index):
            if index >= length:
                return 0
            rob_this_house = max_money_from_house(index + 2) + nums[index]
            skip_this_house = max_money_from_house(index + 1)

            return max(rob_this_house, skip_this_house)
        
        return max_money_from_house(0)
