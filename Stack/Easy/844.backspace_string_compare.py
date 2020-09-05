"""
844. Backspace String Compare
-----------------------------
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def convertToString(string):            
            stack = []
            for char in string:
                if char!='#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
                    else:
                        pass
            return "".join(stack)
        
       
        return convertToString(S) == convertToString(T)
    
"""
Runtime: 32 ms, faster than 21.55% of Python online submissions for Backspace String Compare.
Memory Usage: 12.6 MB, less than 95.63% of Python online submissions for Backspace String Compare.
"""