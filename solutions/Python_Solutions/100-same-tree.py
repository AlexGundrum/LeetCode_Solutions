'''
https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
idea: recurse through both trees, probably dfs, if vals are not ==, return false up?


'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def dfs(p, q):
            if p and q:
                #both have values, lets check to see if they are same
                if p.val != q.val:
                    return False
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            elif not p and not q:
                #both are null, thus same values, so this is fine, return true up
                return True
            else:
                #one is null one is not null. clearly not same tree
                return False
        
        return dfs(p,q)



