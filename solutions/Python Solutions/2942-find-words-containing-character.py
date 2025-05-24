'''
https://leetcode.com/problems/find-words-containing-character/description/?envType=daily-question&envId=2025-05-24

You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.


This is daily question BTW. very easy.
'''


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans
