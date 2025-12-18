'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
idea:
need to do dfs search, because ancestors values matter
maybe keep track of "max val" we've seen in this specific line going down


'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        if not root:
            return 0
        def dfs(root, highestSeen):
            if not root:
                return
            if root.val >= highestSeen:
                nonlocal total
                total += 1
            dfs(root.left, max(root.val, highestSeen))
            dfs(root.right, max(root.val, highestSeen))
        dfs(root, root.val)
        return total




