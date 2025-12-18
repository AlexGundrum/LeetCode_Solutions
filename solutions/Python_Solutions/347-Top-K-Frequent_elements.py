'''
https://leetcode.com/problems/top-k-frequent-elements/description/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

'''

class Solution(object):
    def topKFrequent(self, nums, k):
        nums_seen = set()
        count = defaultdict(int)
        for num in nums:
            nums_seen.add(num)
            count[num] += 1
        
        list_of_nums =  list(nums_seen)
        list_of_nums.sort(key=lambda x: count[x], reverse=True)
        return list_of_nums[:k]
        
