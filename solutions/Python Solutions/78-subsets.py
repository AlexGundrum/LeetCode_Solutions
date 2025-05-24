'''
https://leetcode.com/problems/subsets/description/
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            temp = ans.copy()
            for subset in temp:
                copy = subset.copy()
                copy.append(num)
                ans.append(copy)
        return ans

  
