"""
Write a program to find the node at which the intersection of two singly linked lists begins.


Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ## Method 1 - Hashmap
        # hashmap = {}
        
        # while headA is not None:
        #     hashmap[headA] = headA.next
        #     headA = headA.next
            
        
        # while headB is not None:
        #     if headB in hashmap:
        #         return headB
        #     headB = headB.next
            
        # return None

        ## Method 2 - Two Pointers
        if headA is None or headB is None:
            return None
        
        p1, p2 = headA, headB
    
        while p1!=p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        return p1
                
"""
Runtime: 180 ms, faster than 99.49% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 42.6 MB, less than 97.94% of Python online submissions for Intersection of Two Linked Lists.
"""
                
    
