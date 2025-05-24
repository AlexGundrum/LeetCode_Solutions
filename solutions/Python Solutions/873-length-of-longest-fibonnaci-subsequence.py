'''
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/?envType=daily-question&envId=2025-03-06
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

beat 89% wooo!
'''



'''
idea:
make arr into a set, so we can check if vals exist quickly
loop thru to find first two, then have while loop to see if sequence continues
'''

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        longest = 0
        arrSet = set(arr)
        for a in range(len(arr)):
            for b in range(a + 1, len(arr)):
                if arr[a] + arr[b] in arrSet:
                    num1, num2 = arr[a], arr[b]
                    cur = 2
                    while num1 + num2 in arrSet:
                        cur += 1
                        longest = max(longest, cur)
                        temp = num1
                        num1 = num2
                        num2 = temp + num2
        return longest
