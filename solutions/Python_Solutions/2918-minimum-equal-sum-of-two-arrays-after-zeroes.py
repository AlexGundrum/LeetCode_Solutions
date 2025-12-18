'''
https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/submissions/1696939875/
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.
'''


'''
thoughts
if one array has no zeroes, and a greater sum than the aray with zeroes, impossible, return -1

once we get rid of array equaling one  another and impossible
is it just max( (oneSum + oneZeroes) , (twoSum + twoZeroes) )

'''

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        oneZeroes, twoZeroes = 0, 0
        for num in nums1:
            if num == 0:
                oneZeroes += 1
        
        for num in nums2:
            if num == 0:
                twoZeroes += 1
        
        oneSum, twoSum = sum(nums1), sum(nums2)

        if (oneSum == twoSum and oneZeroes == twoZeroes):
            return oneSum + oneZeroes
        
        if (oneZeroes == 0 and oneSum < (twoSum + twoZeroes)) or (twoZeroes == 0 and twoSum < (oneSum + oneZeroes)):
            #the array with no zeroes is less than value of array that has to increase its value
            return -1
        
        ans = max((oneSum + oneZeroes), (twoSum + twoZeroes))
        return ans
