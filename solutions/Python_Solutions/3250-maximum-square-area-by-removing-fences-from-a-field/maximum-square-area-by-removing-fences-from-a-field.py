'''
ok you got m-1 x n-1 rect field, corners at 1,1 -> mn

there are some fences (the vert n horz go all the way)

there are yo's on the outside

get the max area that can be made of a SQUARE field removing some or all of 

ok so lowkizzle we want to know every distance between the horz and the vertz

like if we have a 0, 3, 5, 9

we then can have for that dim, 2, 3, 5, 6, 9

then whichever of those are in the vert, that is the best we can do ** 2

with 600 length can we do this n^2? 

prob. YOLO!


REMEMNER this is one based
'''


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        modulo = 10 ** 9 + 7

        answer = -1
        #vertDistances = set()
        horzDistances = set()
        #add the four jonsons
        #hFences.append(1)
        #hFences.append(n)
        #vFences.append(1)
        #vFences.append(m)
        hFences.append(m)
        hFences.append(1)
        for i in range(len(hFences)):
            horzDistances.add(abs(hFences[i] - 1))
            horzDistances.add(abs(hFences[i] - m))
            for j in range(i + 1, len(hFences)):
                dist = abs(hFences[i] - hFences[j])
                horzDistances.add(dist)
        
        inBoth = set()
        if (n - 1) in horzDistances:
            inBoth.add(n-1)
        for i in range(len(vFences)):
            ans1 = abs(vFences[i] - 1)
            ans2 = abs(vFences[i] - n)
            
            if ans1 in horzDistances:
                inBoth.add(ans1)
            
            if ans2 in horzDistances:
                inBoth.add(ans2)

            for j in range(i + 1, len(vFences)):
                dist = abs(vFences[i] - vFences[j])
                if dist in horzDistances:
                    inBoth.add(dist)
        
        if len(inBoth) == 0:
            return -1


        answer = max(inBoth) ** 2

        return answer % modulo