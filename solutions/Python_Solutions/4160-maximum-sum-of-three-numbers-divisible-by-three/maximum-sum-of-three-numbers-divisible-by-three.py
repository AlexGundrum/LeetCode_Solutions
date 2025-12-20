'''
given arr nums, we get to sum 3 nums that sum is divis by 3, we want to maximmize this sum
our options are lowkey: 

zero zero zero
zero one two
one one one 
two two two


'''


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        zero, one, two = [], [], []

        for num in nums:
            if num % 3 == 0:
                zero.append(num)
            if num % 3 == 1:
                one.append(num)
            if num % 3 == 2:
                two.append(num)
    

        zero.sort(reverse=True)
        one.sort(reverse=True)
        two.sort(reverse=True)

        
    
        ans = 0
        if len(zero) > 2:
            bigThree = zero[0] + zero[1] + zero[2]
            ans = max(ans, bigThree)
        
        if len(zero) > 0 and len(one) > 0 and len(two) > 0:
            big = zero[0] + one[0] + two[0]
            ans = max(ans, big)
        
        if len(one) > 2:
            big = one[0] + one[1] + one[2]
            ans = max(ans, big)
        
        if len(two) > 2:
            big = two[0] + two[1] + two[2]
            ans = max(ans, big)

        return ans
