'''
ok nums 1 is subset of nums 2

for each element in nums1, return the index of next greater element in nums 2

both arrs are distinct


'''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {}

        for i, num in enumerate(nums2):
            index[num] = i
        
        stack = []
        nextGreater = [-1] * len(nums2)

        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                popped = stack.pop()
                nextGreater[popped] = i
            
            stack.append(i)
        
        ans = [-1] * len(nums1)

        for i, num in enumerate(nums1):
            if nextGreater[index[num]] != -1:
                ans[i] = nums2[nextGreater[index[num]]]
            else:
                ans[i] = -1
        
        return ans