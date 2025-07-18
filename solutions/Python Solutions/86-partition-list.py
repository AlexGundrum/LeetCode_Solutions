'''
https://leetcode.com/problems/partition-list/description/?envType=problem-list-v2&envId=linked-list
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
idea:
lessThan list, greaterThan list
go thru list, if less than append to less, 
then go thru less, have them next into one another
last thing in less .next = first in greater than
go thru greater than, .next into one aniother
last in greater .next = None
if lessThanList return lessthan[0]
else return greater[0]

'''

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        lessThan, greaterThan = [], []
        temp = head
        while temp:
            if temp.val < x:
                lessThan.append(temp)
            else:
                greaterThan.append(temp)
            temp = temp.next
        
        for i in range(len(lessThan) - 1):
            lessThan[i].next = lessThan[i + 1]
        
        for i in range(len(greaterThan) - 1):
            greaterThan[i].next = greaterThan[i + 1]


        if not lessThan: 
            return greaterThan[0]
        
        if not greaterThan:
            return lessThan[0]
        
        lessThan[-1].next = greaterThan[0]
        greaterThan[-1].next = None

        return lessThan[0]














