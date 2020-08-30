"""
1566. Detect Pattern of Length M Repeated K or More Times
---------------------------------------------------------
Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.
A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions. Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.

Example 1:
Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
"""
class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        i = 0
        while i <= len(arr)-1:
            prod = arr[i:i+m]
            if prod * k == arr[i:i+m*k]:
                return True

            i += 1

        return False
                
            

"""
Runtime: 28 ms, faster than 100.00% of Python online submissions for Detect Pattern of Length M Repeated K or More Times.
Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Detect Pattern of Length M Repeated K or More Times.

"""
