'''
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        smallest_word_len = 1000
        for word in strs:
            smallest_word_len = min(smallest_word_len, len(word))
        
        common_prefix = ""
        for i in range(smallest_word_len):
            curr_char = strs[0][i]
            for word in strs:
                if word[i] != curr_char:
                    return common_prefix
            common_prefix = common_prefix + curr_char
        return common_prefix
        
