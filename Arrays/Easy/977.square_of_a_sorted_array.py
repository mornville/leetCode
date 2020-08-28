"""
977. Squares of a Sorted Array
------------------------------
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
class Solution(object):
    def sortedSquares(self, A):
        n = len(A)
        positive = 0
        while positive < n and A[positive] < 0:
            positive += 1
        negative = positive - 1

        ans = []
        while 0 <= negative and positive < n:
            if A[negative]**2 < A[positive]**2:
                ans.append(A[negative]**2)
                negative -= 1
            else:
                ans.append(A[positive]**2)
                positive += 1

        while negative >= 0:
            ans.append(A[negative]**2)
            negative-= 1
        while positive < n:
            ans.append(A[positive]**2)
            positive += 1

        return ans
        
        """ One line solution"""
        # return sorted(num*num for num in A) 
"""
-> Runtime: 204 ms, faster than 76.35% of Python online submissions for Squares of a Sorted Array.
-> Memory Usage: 14.7 MB, less than 58.23% of Python online submissions for Squares of a Sorted Array.
"""