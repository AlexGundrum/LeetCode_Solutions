'''
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/?envType=daily-question&envId=2025-03-06
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
'''


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        posmaxSum = 0
        cursum = 0
        #kadane's algorithm forward pass
        for num in nums:
            cursum = max(0, cursum) # if our cursum is negative, leave it in the past
            #we would rather just start with zero going forward. 
            cursum += num
            posmaxSum =  max(posmaxSum, cursum)
        
        #kadane's algorithm for negative values:
        negativeSum, negativeMax = 0, 0
        
        for num in nums:
            negativeSum = min(0, negativeSum)
            negativeSum += num
            negativeMax = min(negativeMax, negativeSum)
        
        return max(abs(negativeMax), posmaxSum)
