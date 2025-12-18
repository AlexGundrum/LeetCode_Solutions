'''
https://leetcode.com/problems/valid-anagram/description/

242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;

        sMap = {}
        tMap = {}

        for i in range(0, len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        for i in range(0, len(s)):
            if sMap.get(s[i], 0) != tMap.get(s[i], 0):
                return False

        return True