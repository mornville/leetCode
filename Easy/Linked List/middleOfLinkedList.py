# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        a = []
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        itr = slow
        ## output linked list
        while itr:
            a.append(itr)
            itr = itr.next
        return a[0]
    