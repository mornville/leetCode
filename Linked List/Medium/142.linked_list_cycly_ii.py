"""
142. Linked List Cycle II
-------------------------
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next  
            if slow==fast:
                ## traversing again from start to find the start of the cycle, because if slow == fast, it could be either the head or the tail 
                slow=head
                while slow:
                    if slow==fast:
                        return slow
                    slow=slow.next
                    fast=fast.next
        return None
    
"""
-> Runtime: 36 ms, faster than 95.35% of Python online submissions for Linked List Cycle II.
-> Memory Usage: 19 MB, less than 95.43% of Python online submissions for Linked List Cycle II.
"""