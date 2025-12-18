'''
beat 90%!

https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, return the longest palindromic substring in s.
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen, maxSeen = 1, s[0]
        length = len(s)
        for i in range(0, length - 1):
            l, r = i - 1, i + 1

            while l >=0 and r < length:
                if s[l] == s[r]:
                    if (r - l + 1) > maxLen:
                        maxLen = (r - l + 1)
                        maxSeen = s[l: r + 1]
                    l -= 1
                    r += 1
                else:
                    l = -1
            
            if s[i] == s[i + 1]:
                if 2 > maxLen:
                    maxLen = 2
                    maxSeen = s[i:i+2]
                l, r = i - 1, i + 2
                while l >= 0 and r < length:
                    if s[l] == s[r]:
                        if (r - l + 1) > maxLen:
                            maxLen = (r - l + 1)
                            maxSeen = s[l: r + 1]
                        l -= 1
                        r += 1
                    else:
                        l = -1
                
        
        return maxSeen
