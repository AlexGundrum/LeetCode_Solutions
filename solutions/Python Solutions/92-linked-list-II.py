'''
https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=problem-list-v2&envId=linked-list
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
0(n) memory tho
ok we could make a list of the nodes
then its trivial
'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        
        if left != 1:
            l = nodes[0 : left - 1]
        else:
            l = []
        
        mid = nodes[left - 1 : right]
        if right != len(nodes):
            r = nodes[right : len(nodes)]
        else:
            r = []
        
        mid.reverse()
        
        order = l + mid + r

        for i in range(len(order)):
            if i != len(order) - 1:
                order[i].next = order[i + 1]
        
        order[-1].next = None
        return order[0]

        
        
