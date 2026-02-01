class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0]
        smallest, secondSmallest = 61, 61

        for i in range(1, len(nums)):
            num = nums[i]
            if num < smallest and num < secondSmallest:
                secondSmallest = smallest
                smallest = num
                
            elif num < secondSmallest:
                secondSmallest = num
        
        return cost + smallest + secondSmallest