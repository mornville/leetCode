"""
2. Add Two Numbers
------------------
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        ansNode = ListNode(0)
        p3 = ansNode
        tempVal = ListNode(0)
        carry = 0
        
        while p1 is not None and p2 is not None:
            tempVal.val = (p1.val + p2.val + carry)%10 
            p3.next = tempVal
            p3 = p3.next
            carry = (p1.val + p2.val + carry)//10
            p1 = p1.next
            p2 = p2.next
            tempVal = ListNode(0)
    
        ## when len(l1) > len(l2)        
        while p1 is not None:
            tempVal.val = (p1.val + carry) % 10
            p3.next = tempVal
            p3 = p3.next
            carry = (p1.val + carry) // 10           
            p1 = p1.next
            tempVal = ListNode(0)
            
        
        ## when len(l1) < len(l2)
        while p2 is not None:
            print('in p2')
            tempVal.val = (p2.val + carry) % 10
            p3.next = tempVal
            p3 = p3.next
            carry = (p2.val + carry) // 10                      
            p2 = p2.next
            tempVal = ListNode(0)
            
        ## check if any carry is left after adding last digits
        if carry:
            tempVal.val = carry
            p3.next = tempVal
            p3 = p3.next
            
        return ansNode.next

"""
-> Runtime: 52 ms, faster than 96.54% of Python online submissions for Add Two Numbers.
-> Memory Usage: 12.7 MB, less than 67.53% of Python online submissions for Add Two Numbers.
"""