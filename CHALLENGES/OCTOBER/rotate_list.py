"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        lis = []
        cur = head
        while cur != None:
            lis.append(cur.val)
            cur = cur.next
        n = len(lis)
        k = k%n
        self.reverse(lis,n-k,n-1)
        self.reverse(lis,0,n-k-1)
        self.reverse(lis,0,n-1)
        temphead = None
        prev = None
        cur = None
        j = 0
        while j < len(lis):
            if temphead == None:
                temphead = ListNode(lis[j])
                prev = temphead
                j = j + 1
            else:
                cur = ListNode(lis[j])
                prev.next = cur
                prev = cur
                cur = cur.next
                j = j + 1
        return temphead
                
    def reverse(self,lis,start,end):
        while start < end:
            temp = lis[start]
            lis[start] = lis[end]
            lis[end] = temp
            start = start + 1
            end = end - 1
