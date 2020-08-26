"""
1380. Lucky Numbers in a Matrix
-------------------------------
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""

class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if rows:
            col = len(matrix[0])
        else:
            return
        
        minRows, maxCols = [], []
        for i in range(0, rows):
            minRow = pow(10,5)
            for j in range(0, col):
                if matrix[i][j] < minRow:
                    minRow = matrix[i][j]
            minRows.append(minRow)
            
        for j in range(0, col):
            maxCol = 0
            for i in range(0, rows):
                if matrix[i][j] >maxCol:
                    maxCol = matrix[i][j]
            maxCols.append(maxCol)

        return [value for value in maxCols if value in minRows]
    
"""
-> Runtime: 108 ms, faster than 93.24% of Python online submissions for Lucky Numbers in a Matrix.
-> Memory Usage: 13.1 MB, less than 38.43% of Python online submissions for Lucky Numbers in a Matrix
"""