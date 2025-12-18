class Solution:
    def maxDistinct(self, s: str) -> int:
        #wait is it just the number of unique characters? 
        #aaabaa
        #i feel like each new char will just include all of the next characters till the next one
        return len(set([char for char in s]))