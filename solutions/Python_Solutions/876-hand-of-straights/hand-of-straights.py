'''
ok so if len(hand) % groupSize != 0 false. 

then we ougghta sort. i get why this is a greedy problem. 

we must start with the smallest number available. then we take the next
GS - 1 consecutive elements because we have to. 

we continue until we run out of cards and succeed

or until there exists a successor that we don't have



'''


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        counts = defaultdict(int)
        for num in hand:
            counts[num] += 1
        
        nums = sorted(list(set(hand)))

        l = 0

        numberGroups = n // groupSize

        for i in range(numberGroups):
            firstNum = nums[l]
            counts[firstNum] -= 1

            for j in range(1, groupSize):
                #print(counts)
                if counts[firstNum + j] == 0:
                    #print(counts)
                    #print("i= " + str(i))
                    #print("we ran outta: " + str(firstNum + j) + " for " + str(firstNum))
                    return False
                counts[firstNum + j] -= 1

            while (l < len(nums)) and (counts[nums[l]] == 0 ) and counts[firstNum] == 0:
                l += 1
        
        return True
