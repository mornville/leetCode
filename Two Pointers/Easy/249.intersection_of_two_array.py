"""
349. Intersection of Two Arrays
-------------------------------
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
                
        i = 0
        j = 0
        res = set()
        nums1.sort()
        nums2.sort()
        while( i < len(nums1) and j < len(nums2) ):
            if nums1[i] < nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
                continue
            res.add(nums1[i])
            i += 1
            j += 1
        return res
    
"""
-> Runtime: 24 ms, faster than 99.18% of Python online submissions for Intersection of Two Arrays.
-> Memory Usage: 12.7 MB, less than 98.30% of Python online submissions for Intersection of Two Arrays.
"""