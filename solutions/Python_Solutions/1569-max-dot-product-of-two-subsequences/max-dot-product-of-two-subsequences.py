'''
ok so we need to maximize dot product nonempty. 
so weird, we get to choose size of our arrays. 

definitely seems like dp

dp(i, j) -> highest dot product you can get up to indices i,j




'''

from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        
        @lru_cache(maxsize=None)
        def dp(i,j):
            if i >= n1 or j >= n2:
                return 0
        
            double_take = (nums1[i] * nums2[j]) + dp(i+1, j+1)
            take_left = dp(i+1, j)
            take_right = dp(i, j+1)

            return max(double_take, take_left, take_right)
        
        ans = dp(0,0)
        if ans == 0:
            #ok we didn't choose anything which means that one arr is pos, oth negative
            min1, min2 = 1000000, 1000000
            
            for num in nums1:
                if abs(num) < min1:
                    min1 = abs(num)
                
            
            
            for num in nums2:
                if abs(num) < min2:
                    min2 = abs(num)
            return -1 * min1 * min2
            

        return ans