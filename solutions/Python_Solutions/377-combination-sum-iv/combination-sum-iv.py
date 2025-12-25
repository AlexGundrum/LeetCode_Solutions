'''
ok so combinations not permutations 

return number combos. ..  



'''


from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(maxsize=None)
        def dp(amount):
            if amount == 0:
                return 1
            
            if amount < 0:
                return 0
            
            count = 0
            
            for num in nums:
                if num <= amount:
                    count += dp(amount - num)
                else:
                    break

            return count

        

        return dp(target)