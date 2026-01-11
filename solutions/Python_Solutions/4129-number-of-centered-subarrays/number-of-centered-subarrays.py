'''


'''


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for k in range(i, len(nums)):
                ssum = sum(nums[i:k + 1])
                sset = set(nums[i:k+1])
                if ssum in sset:
                    count +=1
        
        return count