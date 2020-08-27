"""
917. Reverse Only Letters
-------------------------
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        
        for char in S:
            if str(char).isalpha():
                stack.append(char)
                
        ans = ''
        
        for char in S:
            if char.isalpha():
                ans+=stack.pop()
            else:
                ans+=char
                
        return ans
    
"""
Runtime: 16 ms, faster than 91.23% of Python online submissions for Reverse Only Letters.
Memory Usage: 12.7 MB, less than 72.81% of Python online submissions for Reverse Only Letters
"""