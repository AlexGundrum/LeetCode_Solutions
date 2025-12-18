'''
https://leetcode.com/problems/add-two-numbers/submissions/1639781670/
2. Add Two Numbers
Solved

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, li1: Optional[ListNode], li2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        l1, l2 = li1, li2
        dummy = ListNode()
        prev = dummy
        while l1 or l2:
            if carry:
                val = 1
            else:
                val = 0
            
            if not l1:
                val += l2.val
                l2 = l2.next
            elif not l2:
                val += l1.val
                l1 = l1.next
            else:
                val += (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next

            new = ListNode(val % 10)
            prev.next = new
            prev = prev.next
            carry = val > 9
        if carry:
            prev.next = ListNode(1)
        
        return dummy.next
            


                 
