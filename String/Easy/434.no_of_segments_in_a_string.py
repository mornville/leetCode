"""
434. Number of Segments in a String
-----------------------------------
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                count +=1
        return count
            
        """ Using builtin split()""" 
        # return len(s.split())

"""
Runtime: 22 ms, faster than 71.11% of Python online submissions for Number of Segments in a String.
Memory Usage: 10.8 MB, less than 87.32% of Python online submissions for Number of Segments in a String.
"""