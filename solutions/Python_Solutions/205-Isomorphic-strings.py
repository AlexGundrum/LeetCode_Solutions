'''
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters_mapped_to = set()
        letters_map = {}
        for i, char in enumerate(s):
            if char in letters_map:
                if letters_map[char] != t[i]:
                    return False
            else:
                if t[i] in letters_mapped_to:
                    return False
                letters_mapped_to.add(t[i])
                letters_map[char] = t[i]
        return True
