"""
27. Remove Element
------------------
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p1 = len(nums) 
        i = 0
        
        while i< p1:
            if nums[i] == val:
                nums[i] = nums[p1-1]
                p1-=1
            else:
                i+=1
        return p1
                
"""
Runtime: 20 ms, faster than 82.73% of Python online submissions for Remove Element.
Memory Usage: 12.7 MB, less than 58.05% of Python online submissions for Remove Element.
"""