'''
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''

class Solution(object):
    def replaceElements(self, arr):
        if len(arr) == 1:
            return [-1]

        final_arr = [0] * len(arr)
        final_arr[-2] = arr[-1]
        final_arr[-1] = -1
        
        for i in range(len(arr) - 3, -1, -1):
            final_arr[i] = max(final_arr[i + 1] , arr[i + 1])
        return final_arr
