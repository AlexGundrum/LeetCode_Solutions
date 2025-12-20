'''
we have array of nums, bin string s. same len

at each index where our string has '1' we get to add that nums[index] to our score. 

it appears we can move our one's down the line but not forward. (to lower indices)


i think we gotta go greedy here. if we see a '1' at index i, we would want it to be moved down to the largest
num at i or lower that has not yet been used by a '1' 

use a max heap then use greedy n pray thats optimal


'''

import heapq
class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        maxheap = []
        score = 0
        LEN = len(nums)
        for i in range(LEN):
            heapq.heappush(maxheap, -nums[i])

            if s[i] == '1':
                #we are gonna use it on the biggest thing we have seen so far that is n't used
                val = -1 * heapq.heappop(maxheap)
                score += val
            

        return score