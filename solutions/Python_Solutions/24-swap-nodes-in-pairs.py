'''
https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=problem-list-v2&envId=linked-list
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        first, second = [], []
        count = 0
        tempHead = head
        while tempHead:
            if count % 2 == 0:
                first.append(tempHead)
            else:
                second.append(tempHead)
            count += 1
            tempHead = tempHead.next
        
        if count == 1:
            return head

        
        '''
        okay so now we snake thru the lists
        second[i].next = first[i]
        first[i].next = second[i + 1]
        ''' 
        f, s = len(first), len(second) #first can be equal to or one greater than second
        
        if f == s:
            for i in range(s):
                second[i].next = first[i]
                if i == s - 1:
                    #we are at the end, need
                    first[i].next = None
                else:
                    #normal
                    first[i].next = second[i + 1]
        else:
            for i in range(s):
                second[i].next = first[i]
                if i == s - 1:
                    #end
                    first[i].next = first[i + 1]
                    first[i + 1].next = None
                else:
                    #normal
                    first[i].next = second[i + 1]
                

        

        return second[0]
