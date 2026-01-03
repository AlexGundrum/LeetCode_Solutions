'''
grid n x 3 

no two johnsons can be same color either vert or horz. 

count number of ways you can paint this. 

definitely dp or just a mathematical answer

or is it a combinatorics thing? 

there are the 12 different ways you can have a legal 1 row

then from there... 

ok it seems like there are really two patterns these things can be in

c1 c2 c1 

or 

c1 c2 c3

if you have a sandwich one then 

c1 c2 c1

then u can do 
c2 c1 c2
c3 c1 c3
c2 c3 c2


121
123
131
132

212
213
231
232

312
313
321
323


so if ur in a sandwich, there are 3 options you can cycle to 

if ur in a stair, there are 3 options you can cycle to 

so for stair meta: 
6 to start * 3 * 3 * 3
+ 
6

u either can start with stair or sandwich

there are 6 of each. 

when you stand on each of those six, there are 3 you can go to at each step. 

ok so you have
for each of the 12 it seems like you get
12 first option: for each of those, 3 second options. 

is there ever a state that you are in where there isn't 3 options next? 

abc

cab
bcb
bab
bca


'''

from functools import lru_cache
class Solution:
    def numOfWays(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, isStair):
            if i == 1:
                return 1
            
            if isStair:
                return 2 * dp(i -1, False) + 2 * dp(i - 1, True)
            else:
                return 3 * dp(i - 1, False) + 2 * dp(i - 1, True)

        modulo = 10 ** 9 + 7

        count = 6 * dp(n, True) + 6 * dp(n, False)
        return count % modulo 