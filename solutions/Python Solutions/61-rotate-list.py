'''
https://leetcode.com/problems/rotate-list/?envType=problem-list-v2&envId=linked-list

Given the head of a linked list, rotate the list to the right by k places.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        
        numberOfNodes = len(nodes)

        realShift = k % numberOfNodes
        if numberOfNodes == 0:
            return head
        
        nodes[-1].next = nodes[0]
        #nodes[-realShift].next = nodes[0]

        nodes[-realShift - 1].next = None
        
        return nodes[-realShift]
