'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
idea - do like kadane's algorithm but in tree form????
we only have to return the value of the max we saw, not the path itself

it'll either be 
    node.left + node.val + node.right
or
    ancestor down to some amount of its descendants

'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        curMax = float('-inf')
        

        def dfs(root):
            nonlocal curMax
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftandright = leftMax + root.val + rightMax
            left = leftMax + root.val
            right = rightMax + root.val
            curMax = max(curMax, leftandright)
            curMax = max(curMax, left)
            curMax = max(curMax, right)
            return max(left, right, root.val, 0)
        
        dfs(root)
        return curMax





