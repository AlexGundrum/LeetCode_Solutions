'''
https://leetcode.com/problems/plus-one/description/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1

        #This means no "carrying the one" so increment the least significant digit and return digits
        if digits[index] < 9:
            digits[index] = 1 + digits[index]
            return digits

        #go down the digits, if value of digit is less than nine, increment and return digits
        #if value of digit == 9, keep going. 
        while index >= 0:
            if digits[index] < 9:
                digits[index] = 1 + digits[index]
                return digits
            else:
                digits[index] = 0
            index = index - 1
        digits[0] = 0
        digits.insert(0,1)
        return digits
