'''
https://leetcode.com/problems/is-subsequence/description/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

'''

class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        
        sub_len, full_len = len(s), len(t)
        sub, full = 0, 0
        
        while sub < sub_len and full < full_len: 
            if s[sub] == t[full]:
                sub, full = sub + 1, full + 1
            else:
                full +=  1
        return sub == sub_len

