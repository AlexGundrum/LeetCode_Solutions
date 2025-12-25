'''
ok count how many strings of length n can be made under rules

a -> e
e -> a,i
i -> a,e,o,u
o -> i, u
u -> a

'''

from functools import lru_cache

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modulo = 10 ** 9 + 7

        let = {
            'a' : ['e'],
            'e' : ['a', 'i'],
            'i' : ['a', 'e', 'o', 'u'],
            'o' : ['i', 'u'],
            'u' : ['a']
        }

        
        @lru_cache(maxsize = None)
        def dp(LEN, lastLet):
            if LEN == n:
                return 1
            
            total = 0
            for char in let[lastLet]:
                total += dp(LEN + 1, char)
            
            return total


        total_count = 0
        for char in 'aeiou':
            total_count += dp(1, char)
        
        return total_count % modulo