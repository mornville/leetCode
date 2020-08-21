# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if head==None:
            return head
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        next = slow.next
        slow.next = None
        slow = next
        
        ## Reversing next list
        p1, prev = head, None
        slow = next
        
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
            
        ## Merge reversed list and slow one by one node
        
        while p1 and prev:
            next1 = p1.next
            next2 = prev.next
            p1.next = prev
            prev.next = next1
            p1 = next1
            prev = next2
            
        
            
            
        