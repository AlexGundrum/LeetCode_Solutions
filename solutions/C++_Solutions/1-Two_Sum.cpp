/*
https://leetcode.com/problems/two-sum/description/
1.
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;

        //we know that two of the elements must add to the target
        //when we arrive at the second element of the two that sum to the target, we need to know the index of the first element.
        //that is we insert the index of what we are at, but the compliment (relative to the target) as our key.
        //so that when we are at the second element, we can use that as the key to get the index
        for (int i = 0; i < nums.size(); i++) {
            if (map.find(nums[i]) == map.end() ){
                map.insert({(target - nums[i]), i});
            }else{
                return {map.at(nums[i]), i};
            }
        }
    }
};
