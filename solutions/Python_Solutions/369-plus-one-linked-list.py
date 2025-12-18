'''
https://leetcode.com/problems/plus-one-linked-list/description/?envType=problem-list-v2&envId=linked-list
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        
        nodes.reverse()
        i = 0
        while i < len(nodes) and nodes[i].val == 9:
            nodes[i].val = 0
            i += 1
        if i != len(nodes):
            #we need to just increment this next value
            nodes[i].val += 1
        else:
            #we need to make a new thing a 1, have it be a new digit node
            new = ListNode(1, nodes[-1])
            head = new

        return head
