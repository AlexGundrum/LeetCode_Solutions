'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
https://leetcode.com/problems/longest-consecutive-sequence/description/

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums)) #Kills all duplicate values
        nums.sort() 
      #Kill all duplicate values, have list sorted in ascending order
        
        curstreak, maxstreak = 1, 1
        for i in range (len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                curstreak += 1
                maxstreak = max(maxstreak, curstreak)
            else:
                curstreak = 1
        #Keep track of the current consecutive sequence, and the largest thus far seen sequence. 
        return maxstreak
        #Return the maximum sequence length seen
