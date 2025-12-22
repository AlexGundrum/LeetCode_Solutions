'''
ok so we delete stuff and have to make the strings equal

we want ascii sum to be minijmized

dp(i,j):
min cost to make s1[:i] == s2[:j]

base cases: 
if both are in bounds and ==, just go to dp i + 1, j + 1

if both are oob return 0

if one is oob and other isn't we need to delete the rest of the in bounds. 

if both are in bounds and not equal, try deleting each and return min. 

'''
from functools import lru_cache

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @lru_cache(maxsize = None)
        def dp(i, j):
            if (i >= len(s1) and j >= len(s2)):
                return 0 #both oob
            
            if (i >= len(s1)):
                #i is oob
                return sum(ord(c) for c in s2[j:])

            if (j >= len(s2)):
                #j is oob
                return sum(ord(c) for c in s1[i:])
            
            #both are in bounds. 
            if s1[i] == s2[j]:
                #equal, no deletes needed
                return dp(i + 1, j +1)
            
            leftDel = ord(s1[i]) + dp(i + 1, j)
            rightDel = ord(s2[j]) + dp(i, j + 1)

            return min(leftDel, rightDel)

        return dp(0,0)
    