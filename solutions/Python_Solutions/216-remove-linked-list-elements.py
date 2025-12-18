'''
https://leetcode.com/problems/remove-linked-list-elements/description/?envType=problem-list-v2&envId=linked-list
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        firstThing = None
        prevThing = None

        temp = head
        while temp:
            if temp.val != val:
                if not firstThing:
                    firstThing = temp
                    prevThing = temp
                else:
                    prevThing.next = temp
                    prevThing = temp

            temp = temp.next
        
        if not firstThing:
            return None
        
        prevThing.next = None
        return firstThing
