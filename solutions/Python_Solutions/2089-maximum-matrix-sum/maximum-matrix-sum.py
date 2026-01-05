'''
ok so any two things that are adj can get *= -1

maximize sum of elements. 

i feel like if theres even amount of neg numbers u can get them
all to be positive

if theres odd amount then you just make the smallest val to be the negative one left

'''


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        minSeen = 10 ** 10
        negativeCount = 0
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                curnum = matrix[x][y]
                minSeen = min(minSeen, abs(curnum))
                
                totalSum += abs(curnum)
                
                if curnum < 0:
                    negativeCount += 1
        
        print("total: " + str(totalSum) + " min: " + str(minSeen) + " negcoun: " + str(negativeCount))
        if negativeCount % 2 == 0:
            return totalSum
        else:
            return totalSum - 2 * minSeen
        