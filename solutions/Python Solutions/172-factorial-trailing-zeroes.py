'''
https://leetcode.com/problems/factorial-trailing-zeroes/description/?envType=study-plan-v2&envId=top-interview-150
Given an integer n, return the number of trailing zeroes in n!.

'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 5
        count = 1
        total = 0
        while num < n:
            num *= 5
            count += 1

        while count > 0:
            total += (n// (5 ** count))
            count -= 1
        return total



