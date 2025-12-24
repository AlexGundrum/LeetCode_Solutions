class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        index = 0
        count = 0
        while total > 0:
            total -= capacity[index]
            index += 1
            count += 1
        
        return count
        