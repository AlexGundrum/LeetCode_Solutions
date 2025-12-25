'''
have domino and tromino

given int n, ret number of ways to tile 2xn board. 
return modolu 109 + 7


dp(top, bot) -> number of ways you can fill that num of tiles

ok so if top or bottom > n, ret 0

at each step
we can:
top + 2
bot + 2
top + 1, bot + 1
top + 1, bot + 2
top + 2, bot + 1


didn't initially work. should top + 2, bottom + 2 be same thing? 


if at a spot you choose to have a domino horz, the next step just will be to also lay it down horz too.
wait thats also wrong.....


'''

from functools import lru_cache
class Solution:
    def numTilings(self, n: int) -> int:
        
        modulo = (10 ** 9) + 7


        @lru_cache(maxsize = None)
        def dp(top, bottom):
            if top == n and bottom == n:
                return 1
            elif top > n or bottom > n:
                return 0
            
            options = []
            if top == bottom:
                options = [[2,2],  [1,1], [1,2], [2,1]]
            
            elif top > bottom:
                options = [[0,2] , [1,2]]
            else:
                options = [[2,0], [2,1]]
            
            total = 0

            for a, b in options:
                total += dp(top + a, bottom + b)
            
            return total

        count = dp(0, 0)
        
        return int(count % modulo)