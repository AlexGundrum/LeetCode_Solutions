'''
https://leetcode.com/problems/validate-binary-search-tree/description/
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
idea: 
for left subtree, we need to find max value. 
if max value of left sub tree < root.val, left side is valid
for right subtree, find min value
if min val of right subtree > root.val, right side is valid

do this but recursively down tree


idea 2, inspired by hints (redo raw later)
have dfs have greater than and less than values to ensure it is within bounds of bst


'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, mustBeLessThanVal, mustBeGreaterThanVal):
            if not root:
                return True
            if not (mustBeGreaterThanVal < root.val < mustBeLessThanVal):
                return False
            else:
                return dfs(root.left, root.val, mustBeGreaterThanVal) and dfs(root.right, mustBeLessThanVal,root.val )
            
        return dfs(root, float("inf"), float("-inf"))

  
