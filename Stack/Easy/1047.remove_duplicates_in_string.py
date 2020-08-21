"""
1047. Remove All Adjacent Duplicates In String
----------------------------------------------
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Example 1:
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

"""
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for char in S:
            if not stack:
                stack.append(char)
            else:
                if stack[-1] == char:
                    stack.pop()
                else:
                    stack.append(char)

        return ''.join(stack)

"""
-> Runtime: 52 ms, faster than 99.67% of Python online submissions for Remove All Adjacent Duplicates In String.
-> Memory Usage: 13.1 MB, less than 77.41% of Python online submissions for Remove All Adjacent Duplicates In String.
"""