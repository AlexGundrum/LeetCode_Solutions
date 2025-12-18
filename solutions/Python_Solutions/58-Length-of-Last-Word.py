'''
https://leetcode.com/problems/length-of-last-word/description/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
'''
#LOL this is why I like leetcoding in python!
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])
        
