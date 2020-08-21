"""
1021. Remove Outermost Parentheses
----------------------------------
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

"""

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        p1 = 0
        ans = ''
        while p1<len(S):
            if S[p1] == '(':
                count+=1
                if count>1:
                    ans+=S[p1]
            else:
                count-=1
                if count>0:
                    ans+=S[p1]
            p1+=1
        return ans

"""
-> Runtime: 32 ms, faster than 80.60% of Python online submissions for Remove Outermost Parentheses.
-> Memory Usage: 12.9 MB, less than 72.06% of Python online submissions for Remove Outermost Parentheses.
"""