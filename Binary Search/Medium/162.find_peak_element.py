"""
162. Find Peak Element
----------------------
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if nums[mid] > nums[mid + 1] :
                high = mid
            else:
                low = mid + 1
                
        return low
                    
"""
Runtime: 28 ms, faster than 94.43% of Python online submissions for Find Peak Element.
Memory Usage: 12.9 MB, less than 42.83% of Python online submissions for Find Peak Element.
"""