'''
ok so definitely could binary search this john

50,000
nlgn

lowkey don't know how to easily calc area above n below besides dumma way 

i feel like there's some crazy math ball idk about
'''


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        mini, maxi = 10 ** 11, -1

        def getAreaBelow(y_line):
            area = 0
            for x, y, l in squares:
                if y >= y_line:
                    continue
                if y + l <= y_line:
                    area += l * l
                else: 
                    area += l * (y_line - y)
            return area
        
        totalArea = 0
        
        for x, y, l in squares:
            mini = min(mini, y)
            maxi = max(maxi, y + l)
            totalArea += (l * l)
        
        half = totalArea / 2
        
        #ok lets binary search. 
        l, r = mini, maxi
        #print(f"starting at {l} , {r}")
        smallestSeen = 10 ** 11
        
        while l < r and abs(r - l) > .00001:
            mid = (l + r) / 2
            amtBelow = getAreaBelow(mid)
            #print(f"{mid} has {amtBelow}")

            if abs(amtBelow - half) < .000001:
                #print(f"ding ding ding {mid}")
                smallestSeen = min(smallestSeen, mid)
                r = mid
            elif amtBelow < half:
                #too big,go down
                l = mid
            else:
                #too small, go up
                r = mid 
        
        return r
            

        
