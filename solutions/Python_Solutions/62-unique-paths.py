'''
https://leetcode.com/problems/unique-paths/
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''


'''
plan: top down dp
if you can go right count ways after you go right
if yuo can go down count ways after you go down
then return this sum!



'''

from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def how_many_paths_to_end_from_position(x,y):
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n:
                return 0
            
            paths_if_you_go_right =  how_many_paths_to_end_from_position(x + 1, y)
            paths_if_you_go_down = how_many_paths_to_end_from_position(x, y + 1 )
            return paths_if_you_go_right + paths_if_you_go_down
        
        return how_many_paths_to_end_from_position(0,0)

  
