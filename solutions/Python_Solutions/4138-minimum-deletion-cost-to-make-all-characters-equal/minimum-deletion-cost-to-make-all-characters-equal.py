'''
s only has lowercase letters
default dict letter -> cost
whatever letter has the max cost will be the one we keep. 


'''


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        let_costs = defaultdict(int)
        total = 0
        chars = set()

        for i in range(len(s)):
            char = s[i]
            chars.add(char)
            let_costs[char] += cost[i]
            total += cost[i]
        
        lst = []

        if len(chars) == 1:
            return 0

        for char in chars:
            
            lst.append(let_costs[char])
        
        lst.sort(reverse=True)
        return total - lst[0]