'''
https://leetcode.com/problems/binary-tree-right-side-view/description/
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 
'''

# POTENTIALLY CONFUSING DESCRIPTION! NOT A BALANCED TREE, SO IT ISN'T JUST ROOT.RIGHT WHILE ROOT. NODES ON LEFT SIDE CAN BE VISIBLE FROM RIGHT SIDE,
#ON LEVEL ORDER TRAVERSAL, LAST NODE TRAVERSED IS VISIBLE FROM RIGHT!!!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque()
        
        if root:
            q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                level.append(cur.val)
            ans.append(level[-1])
        return ans
