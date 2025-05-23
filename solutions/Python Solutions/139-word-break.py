'''
https://leetcode.com/problems/word-break/description/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

'''


from functools import cache
'''

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def can_string_be_made_from_dict_words(string):
            #base cases 
            #1) string == dictionary word, return true
            #2) none of the dictionary words appear as the "first" part of the string, return false
            stringLength = len(string)
            for word in wordDict: 
                wordLength = len(word)
                if wordLength > stringLength:
                    continue
                
                if word == string:
                    return True
                newString = string[wordLength : ]
                if word == string[:wordLength] and can_string_be_made_from_dict_words(newString):
                    return True       
            return False
        
        return can_string_be_made_from_dict_words(s)
      
