'''
https://leetcode.com/problems/linked-list-in-binary-tree/
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        

        def dfs(tree, lst):
            if not lst:
                return True
            if not tree and lst:
                return False
            if tree.val != lst.val:
                return False
            
            return dfs(tree.left, lst.next) or dfs(tree.right, lst.next)
        
        q = deque()
        if root:
            q.append(root)
        
        while q:
            popped = q.popleft()
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        
            if dfs(popped, head):
                return True
        
        return False
            
