'''

https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return [seen[(num)], i]
            else:
                seen[target - num] = i
