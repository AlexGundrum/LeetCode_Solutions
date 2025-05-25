'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

'''

'''
can only think of O(m + n) solution

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1, n2 = 0, 0
        length1, length2 = len(nums1), len(nums2)
        new = []
        while n1 < length1 and n2 < length2:
            if nums1[n1] <= nums2[n2]:
                new.append(nums1[n1])
                n1 += 1
            else:
                new.append(nums2[n2])
                n2 += 1
        
        if n1 < length1:
            new += nums1[n1:]
        if n2 < length2:
            new += nums2[n2:]
        
        newlength = len(new)
        if newlength % 2 == 0:
            #even, return avg of middle two 
            return ((new[(newlength - 1) // 2]) + (new[newlength // 2])) / 2
        else:
            #odd, return middle
            return new[(newlength // 2)]

