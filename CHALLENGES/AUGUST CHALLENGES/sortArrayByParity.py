"""
AUGUST 21, SORT ARRAY BY PARITY
-------------------------------
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = 0
        while p2<len(A):
            if A[p2] % 2 == 0:
                print('even')
                temp = A[p2]
                A[p2] = A[p1]
                A[p1] = temp
                p1+=1
            p2+=1
        return A



"""
-> Your memory usage beats 99.57 % of python submissions.
-> Your runtime beats 76.57 % of python submissions.
"""