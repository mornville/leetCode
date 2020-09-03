"""
1221. Split a String in Balanced Strings
----------------------------------------
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        stack.append(-1)
        count = 0
        for char in s:
            if (stack[-1] == 'R' and char == 'L') or (stack[-1] == 'L' and char == 'R'):
                stack.pop()
            else:
                stack.append(char)
            
            if stack[-1] == -1:
                count+=1
                
        return count
    
"""
Runtime: 24 ms, faster than 68.03% of Python online submissions for Split a String in Balanced Strings.
Memory Usage: 12.7 MB, less than 50.16% of Python online submissions for Split a String in Balanced Strings.
"""