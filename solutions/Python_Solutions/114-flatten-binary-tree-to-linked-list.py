'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=linked-list
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        preorderList = []
        def preorder(rot):
            if not rot:
                return
            nonlocal preorderList
            preorderList.append(rot)
            preorder(rot.left)
            preorder(rot.right)
        
        preorder(root)
        for i in range(len(preorderList) - 1):
            preorderList[i].right = preorderList[i + 1]
            preorderList[i].left = None
        
        preorderList[-1].right = None
        preorderList[-1].left = None

        
