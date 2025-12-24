class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        curStart, curEnd = intervals[0][0] , intervals[0][1]

        for i in range(1, len(intervals), 1):
            tStart, tEnd = intervals[i][0], intervals[i][1]
            if tStart <= curEnd:
                #this new interval falls between our current interval. add
                curEnd = max(curEnd, tEnd)
            else:
                #ok we have started a new thing. add old. make this new our cur
                output.append([curStart, curEnd])
                curStart = tStart
                curEnd = tEnd
        
        #i feel like by default we gotta add this last thing. 
        output.append([curStart, curEnd])
        return output
        
        #check last thing. 