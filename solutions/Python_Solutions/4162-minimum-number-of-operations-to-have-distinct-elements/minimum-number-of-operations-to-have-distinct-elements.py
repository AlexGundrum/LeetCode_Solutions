'''
idea

go from right to left, and have a set. we keep track of the elements till we find a duplicate or run out of thigns. 

once we have a duplicate, we break. 

we compare the size of the set to the size of the array. 

we can then deduce the number of 3 eliminations needed. 


'''

import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        LEN = len(nums)

        for i in range(LEN - 1, -1, -1):
            num = nums[i]
            if num in seen:
                break
            seen.add(num)
        
        difference = LEN - len(seen)

        #ok so the number of 3 elims we need to do would be ceil(diff / 3)
        ans = math.ceil(difference / 3)

        return ans
