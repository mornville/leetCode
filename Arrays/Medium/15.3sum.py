"""
15. 3Sum
---------
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = x + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([x, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans

"""
-> Runtime: 596 ms, faster than 85.73% of Python online submissions for 3Sum.
-> Memory Usage: 15.9 MB, less than 86.01% of Python online submissions for 3Sum.
"""