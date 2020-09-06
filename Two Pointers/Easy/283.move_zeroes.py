"""
283. Move Zeroes
----------------
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         for j in range(i+1, len(nums)):
        #             if nums[j] != 0:
        #                 nums[i] = nums[j]
        #                 nums[j] = 0
        #                 break
        
        x=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[x]=nums[i]
                x+=1
        
        while x!=len(nums):
            nums[x]=0
            x+=1

"""
Runtime: 48 ms, faster than 50.47% of Python online submissions for Move Zeroes.
Memory Usage: 13.6 MB, less than 83.21% of Python online submissions for Move Zeroes.
"""