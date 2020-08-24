"""
23. Merge k Sorted Lists
Given an array of linked-lists lists, each linked list is sorted in ascending order.
Merge all the linked-lists into one sort linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        totalLists = len(lists)
        interval = 1   
        
        while interval < totalLists:
            for i in range(0, totalLists-interval, interval*2):
                lists[i] = self.mergeLists(lists[i], lists[i+interval])
            interval = interval*2 
            
        return lists[0]
    
    def mergeLists(self, list1, list2):
        head = temp = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list1
                list1 = temp.next.next
            temp = temp.next
            
        if not list1:
            temp.next = list2
        else:
            temp.next = list1    
            
        return head.next               

"""
-> Runtime: 108 ms, faster than 73.43% of Python online submissions for Merge k Sorted Lists.
-> Memory Usage: 18.8 MB, less than 86.06% of Python online submissions for Merge k Sorted Lists.
"""