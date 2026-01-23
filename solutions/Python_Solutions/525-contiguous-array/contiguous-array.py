'''
ok if we have 0 be put in as negative one, whatever is the longest thing that equals 0 in our 
prefix works


'''


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        asdf = defaultdict(list)
        asdf[0] = [0]
        for i in range(1, n + 1):
            num = 0
            if nums[i - 1] == 0:
                num = -1
            else:
                num = 1
            
            prefix[i] = prefix[i - 1] + num
            asdf[prefix[i]].append(i) #asdf has 
        
        longestSeen = 0
        #print(f"prefix: {prefix}")
        for i in range(1, n + 1):
            dif = prefix[i] #the net difference for first i things
            #if we see that there is 
            compliment = asdf[dif]
            
            if compliment:
                length = i - compliment[0]
                longestSeen = max(longestSeen, length)

        return longestSeen 
