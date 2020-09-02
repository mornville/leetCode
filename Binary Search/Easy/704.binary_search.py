"""
704. Binary Search
------------------
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        return -1
    
"""
-> Runtime: 220 ms, faster than 88.19% of Python online submissions for Binary Search.
-> Memory Usage: 13.5 MB, less than 60.04% of Python online submissions for Binary Search.
"""