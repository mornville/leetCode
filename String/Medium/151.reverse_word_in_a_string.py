"""
151. Reverse Words in a String
Given an input string, reverse the string word by word.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
#         stack = []
#         temp = ""
#         i = 0 
#         while i < len(s):
#             if s[i]!=' ':
#                 temp+=s[i]
#             elif s[i] == ' ' and temp!= "":
#                 stack.append(temp)  
#                 temp = ""
                
#             if i == len(s) - 1 and s[i]!=" ":
#                 stack.append(temp)
                
#             i+=1
        

#         return ' '.join(stack[::-1])

        """ One line solution using split"""
        return ' '.join(s.split()[::-1])


"""
Runtime: 12 ms, faster than 98.24% of Python online submissions for Reverse Words in a String.
Memory Usage: 14 MB, less than 42.69% of Python online submissions for Reverse Words in a String.
"""