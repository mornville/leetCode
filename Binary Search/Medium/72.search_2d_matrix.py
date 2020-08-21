"""
74. Search a 2D Matrix
----------------------
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        rows = len(matrix)
        if rows:
            columns = len(matrix[0])
        
        if rows == 0 or columns == 0 or matrix[0][0]> target:
            return False
        
        low, high = 0, rows*columns-1
        
        while low <= high:
            mid = low + (high-low)//2
            element = matrix[mid/columns][mid%columns]
            if element == target:
                return True
            elif element > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
                
"""
-> Runtime: 52 ms, faster than 80.53% of Python online submissions for Search a 2D Matrix.
-> Memory Usage: 14.6 MB, less than 42.13% of Python online submissions for Search a 2D Matrix.
"""