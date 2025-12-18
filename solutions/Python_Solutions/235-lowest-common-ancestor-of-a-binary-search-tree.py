'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
idea: 
two nodes are descendents of a given node if:
the two nodes are in the subtree of that given node


is it about the properties of a BST, or is it checking subtrees, and lowest subtree
that has both is answer?


thinking about it with properties of BST
if we are on node T and : p.val < t.val < q.val (or q < t < p)
t must be our answer

if we are on node t and our t.val == p.val or q.val, t must be our answer

if t < q < p or t > q > p, we know which child to go down to and check

'''



class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        

        def dfs_helper(curnode, p, q):
            #since p and q will both exist in BST, we know that we will never
            #hit "null value", so we do not need to check for it here
            #base cases:
            #if curnode.val == p.val or q.val, curnode is our answer.
            #if p.val < curnode.val < q.val OR q.val < curnode.val < p.val, curnode is ans
            #if p and q are both larger or smaller than curnode's val, go to left or right child accordingly
            cval, pval, qval = curnode.val, p.val, q.val
            if cval == pval or cval == qval:
                return curnode
            if (pval < cval < qval) or (qval < cval < pval):
                return curnode
            if cval < pval:
                #pval and qval are greater than our value, so recurse down to r child
                return dfs_helper(curnode.right, p, q)
            else:
                #pval and qval are less than our value, recurse down to l child
                return dfs_helper(curnode.left, p, q)

        return dfs_helper(root, p, q)
      
