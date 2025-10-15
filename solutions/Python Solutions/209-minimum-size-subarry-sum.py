'''
https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window&
209. Minimum Size Subarray Sum
Medium
Topics
conpanies icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

'''

'''
all pos integers
min length of subarr whos sum its greater eq to target

'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = 999_999 
        curTotal = 0
        left = 0

        for right in range(len(nums)):
            curNum = nums[right]
            curTotal += curNum
            if curTotal >= target:
                while left <= right and curTotal >= target:
                    minLength = min(minLength, (right - left + 1))
                    toSubtract = nums[left]
                    curTotal -= toSubtract
                    left += 1


        if minLength == 999_999:
            minLength = 0

        return minLength
