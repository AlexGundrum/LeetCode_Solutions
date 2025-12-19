from functools import lru_cache
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        #need to finish at least one task every day
        #the difficulty of a job schedule is sum of difficulties of each day of the d days
        #the dif of a day is max difficulty of a job done on that day

        #return minimum difficulty of a job schedule. 

        #since we must finish a task each day, if len(jd) > d, ret false
        #if num jobs >= d, is there any way we can't find a schedule? 
        if len(jobDifficulty) < d:
            return -1

        #so we want to minimize the min difficulty of job schedule. so we are minimizing the dif
        #the sum of each days difficulties. 
        #ohhhh but for a job in JD, you can only work on it if all before it have been completed.


        #ok lets get overlapping subproblems
        #so each day MUST include the next job lined up. 
        #so when we are on the ith day:
        #we must schedule the next job. then we get to choose how many extra jobs we schedule. 
        #we can schedule until it would make it st a day woudl run out
        #if we are on the last day we MUST schedule until we have done all the jobs.
        LEN = len(jobDifficulty)
        @lru_cache(maxsize=1280)
        def dp(day, jobIndex):
            if day == d:
                return max(jobDifficulty[jobIndex:])

            #now we wanna try all of our options. we can choose as many jobs as we'd like
            #until it would make it so that future days ran out of jobs. 
            futureDays = d - day
            curMax = 0
            options = []
            futures = []
            for i in range(jobIndex, LEN - futureDays, 1):
                curMax= max(curMax, jobDifficulty[i])
                options.append(curMax)
                futures.append(dp(day + 1, i + 1))
            
            totals = [options[i] + futures[i] for i in range(len(options))]
            return min(totals)
        
        return dp(1, 0)
        

        
