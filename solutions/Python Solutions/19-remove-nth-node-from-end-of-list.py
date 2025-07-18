'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        tempHead = head
        while tempHead:
            lst.append(tempHead)
            tempHead = tempHead.next
        
        size = len(lst)
        if size == 1:
            return None

        indexToRemove = size - n

        if indexToRemove == 0:
            return head.next

        lst[indexToRemove - 1].next = lst[indexToRemove].next
        return head         
