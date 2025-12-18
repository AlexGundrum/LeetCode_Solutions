'''
https://leetcode.com/problems/permutations/description/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(cur, arr):
            if len(arr) == 1:
                copy = cur.copy()
                copy.append(arr[0])
                ans.append(copy)
            
            for num in arr:
                copy = arr.copy()
                copy.pop(copy.index(num))
                curCopy = cur.copy()
                curCopy.append(num)
                helper(curCopy, copy)
        
        helper([], nums)
        return ans


