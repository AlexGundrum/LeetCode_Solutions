'''
time based key value ds that stores multiple values for the same key at different time stamps
and retrieves key's value at a certain time stamp

what

ok so we need (key, time) -> value


get
returns a value what set was called previously with, you get something that has a lower 
val than the timestamp passed in

and we need to choose the largest value smaller than our new val



i wonder if we need to BS or if we can have hash map spam

ok we get TLE'd 





'''
from sortedcontainers import SortedList
import bisect

class TimeMap:

    def __init__(self):
        self.key_times_set = defaultdict(set)
        self.key_time_map = {}
        #self.key_last = {}
        self.key_time_list = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.key_times_set[key]:
            self.key_time_list[key].add(timestamp)
            self.key_times_set[key].add(timestamp)
        #self.key_last[key] = timestamp
        self.key_time_map[tuple([key,timestamp])] = value
        

    def get(self, key: str, timestamp: int) -> str:
        #times = self.key_times_set[key]
        ans = ""
        #curTime = -1
        
        lst = self.key_time_list[key]
        index = bisect.bisect_right(lst, timestamp)
        if index == 0:
            return ""

        return self.key_time_map[tuple([key, lst[index - 1]])]

        #return self.key_time_map[tuple([key, self.key_last[key]])]
        #for time in times:
        #    if time <= timestamp and time > curTime:
        #        curTime = time
        #        ans = self.key_time_map[tuple([key, time])]
        
        #return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)