'''
there are n kids, where happiness[i] is hap of ith kid

select k kids in k turns. 

each turn, happiness value of all kids that have not been selected till now dec by one. 
can't go negative though

ret max sum of hap values by grabbiung k kids


i start thinking of a heap... but if we have two kids and 1 1 1 6, we need to select the '1' before the '6'


so ok we make a max heap, grab the top k things. 

then we will sort that, go from smallest to biggest so that we minimize losing out. nope 

1 + 11 + 40

'''


import heapq

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        kids = [-1 * kid for kid in happiness]
        heapq.heapify(kids) 
        chosen = []
        for i in range(k):
            kid = -1 * heapq.heappop(kids)
            chosen.append(kid)

        #chosen = chosen[::-1] #reverse it so that the smallest is first. 

        score = 0
        for i in range(len(chosen)):
            score += max(0, chosen[i] - i)
            print('score: ' + str(score))        
        return score