"""
680. Valid Palindrome II
------------------------
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                # delete left
                one = s[left+1:right+1]
                # delete right
                two = s[left:right]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True

"""
-> Runtime: 84 ms, faster than 89.73% of Python online submissions for Valid Palindrome II.
-> Memory Usage: 13.9 MB, less than 30.81% of Python online submissions for Valid Palindrome II.
"""