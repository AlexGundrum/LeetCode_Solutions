# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

ok product of sums of substrees

ok so maybe we get the total sum of the whole thing

then for each node we get the sum of it and its kids. 
total - that sum = the amount in the other 






'''

from functools import lru_cache
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        modulo = 10 ** 9 + 7
        maxSeen = 0

        @lru_cache(maxsize=None)
        def dfs(root):
            if not root:
                return 0
            
            return root.val + dfs(root.left) + dfs(root.right)

        totalSum = dfs(root)

        queue = deque()

        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            thisSubTreeSum = dfs(node)
            otherTreeVal = totalSum - thisSubTreeSum
            thisMultiplication = thisSubTreeSum * otherTreeVal

            maxSeen = max(maxSeen, thisMultiplication)
        
        return maxSeen % modulo
        #














