'''
in allowed, it goes: left right top

given the bottom, return if you can build pyramid up to top. 

ok so if we do a recursive alg, we only need to keep track of each row at a time

dp prob

ok but how do we form the layer? 
how do we build all of those options? 

ok when given layer of size 3
we know we have two slots to fill. we add that to an arr? or something. 

'''

from functools import lru_cache
import itertools
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        patterns = defaultdict(list)

        for string in allowed:
            two = string[:2]
            top = string[2]
            patterns[two].append(top) 
        
        #ok so now we have our thing
        @lru_cache(maxsize=None)
        def dp(layer):
            if len(layer) == 1:
                return True
            
            options = []

            for i in range(len(layer) - 1):
                left, right = layer[i], layer[i + 1]
                key = left + right
                if key not in patterns:
                    return False
                options.append(patterns[key])
            
            #ok so now we know we have options - options[i] represents all colors the ith thing in next layer could be
            #so how do we weave this to then try all options? 
            #i mean at worst we have 6 ^ 5. 
            permutations = list(itertools.product(*options))
            for perm in permutations:
                if dp(perm):
                    return True
            
            return False
        return dp(bottom)


