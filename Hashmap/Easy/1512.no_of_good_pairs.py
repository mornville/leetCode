"""
1512. Number of Good Pairs
--------------------------
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
 
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = (collections.Counter(nums))
        ans = 0
        
        for count in total.values():
            ans+= (count*(count-1)) // 2
        
        return ans


"""
Runtime: 12 ms, faster than 99.33% of Python online submissions for Number of Good Pairs.
Memory Usage: 12.7 MB, less than 53.61% of Python online submissions for Number of Good Pairs.
"""