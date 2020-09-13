"""
86. Partition List
------------------
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:

            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next
    
"""
Runtime: 28 ms, faster than 47.64% of Python online submissions for Partition List.
Memory Usage: 12.7 MB, less than 86.05% of Python online submissions for Partition List.
"""