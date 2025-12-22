'''
surely 2d. 

maybe the pattern is something like: 

dp(l,r)
if s[l] == s[r] we are gonna add it...
then if not we can shift l 
and shift r? 

ok but how do we know where to start, and if we choose none or one as our middle



oh but we start outside and move in. 

we start at outside and then if l == r then we know we have a length of two. 

add two, shimmy both. 
if l != r, shimmy one? 

then we still need to worry about base case where we can add the one john in the middle. 




'''

from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        @lru_cache(maxsize=None)
        def dp(l, r):
            #base cases
            if not ((0 <= l < len(s)) and (0 <= r < len(s))):
                return 0
            
            if (l > r):
                return 0

            if l == r:
                return 1
                #oob check make sure indicies are valid
            
            if s[l] == s[r]:
                #print(str(l) + " " + str(r))
                return 2 + dp(l + 1, r - 1)
            
            left_shimmy = dp(l + 1, r)
            right_shimmy = dp(l, r - 1)
            return max(left_shimmy, right_shimmy)
        

        

        return dp(0, len(s) - 1)