'''
https://leetcode.com/problems/sort-list/description/?envType=problem-list-v2&envId=linked-list
Given the head of a linked list, return the list after sorting it in ascending order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        nodes.sort(key=lambda x: x.val)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        
        nodes[-1].next = None
        return nodes[0]
