"""
50. Pow(x,n)
------------
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n
        
        curProduct = x
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= curProduct
            
            curProduct *= curProduct
            n //= 2
        
        return res

"""
-> Runtime: 16 ms, faster than 91.47% of Python online submissions for Pow(x, n).
-> Memory Usage: 12.6 MB, less than 94.20% of Python online submissions for Pow(x, n).
"""