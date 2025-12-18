'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ans = [""]
        digitToChar = {
            '2' : "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9' : "wxyz"
        }
        
        def dfs(numRemaining):
            if len(numRemaining) == 0:
                return
            digit = numRemaining[0]
            numRemaining = numRemaining[1:]
            chars = digitToChar[digit]
            temp = []
            nonlocal ans
            for cur in ans:
                for char in chars:
                    copy = cur
                    copy = copy + char
                    temp.append(copy)
            ans = temp
            dfs(numRemaining)




        dfs(digits)
        return ans
