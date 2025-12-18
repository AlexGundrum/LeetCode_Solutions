'''
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        count = 0

        while height[l] == 0 and l < len(height):
            l += 1
        r = l
        while r < len(height):
            if height[r] >= height[l]:
                count += height[l] * (r - l - 1)
                for i in range(l + 1, r, 1):
                    count -= height[i]
                l = r
                r += 1
            else:
                r += 1
        return count
