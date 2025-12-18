'''
https://leetcode.com/problems/subtree-of-another-tree/submissions/1643264504/
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
idea: search through big tree, and if we reach subRoot.val val, we then check to see if they are
the same tree

edge cases:
same tree
root is empty - false unless sub tree is empty?
sub tree is empty
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.dfs(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def dfs(self, p, q):
        if p and q:
            if p.val != q.val:
                return False
            return self.dfs(p.left, q.left) and self.dfs(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False
        
        
