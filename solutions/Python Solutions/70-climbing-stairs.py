'''
https://leetcode.com/problems/climbing-stairs/description/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def count_ways(n):
            if n == 0 or n == 1:
                return 1
            
            return count_ways(n-1) + count_ways(n-2)
        
        return count_ways(n)
