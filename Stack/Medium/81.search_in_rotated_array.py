"""
81. Search in Rotated Sorted Array II
-------------------------------------
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.sort()
        
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right  = mid
        return False
            
"""
-> Runtime: 36 ms, faster than 92.59% of Python online submissions for Search in Rotated Sorted Array II.
-> Memory Usage: 12.9 MB, less than 79.77% of Python online submissions for Search in Rotated Sorted Array II.
"""