"""
345. Reverse Vowels of a String
-------------------------------
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:  
Input: "leetcode"
Output: "leotcede"
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        vowels = 'aeiouAEIOU'
        start = 0
        end = len(s) - 1
        while start < end:
            if ans[start] in vowels and ans[end] in vowels:
                ans[start], ans[end] = ans[end], ans[start]
                start += 1
                end -= 1
            if ans[start] not in vowels:
                start += 1
            if ans[end] not in vowels:
                end -= 1
        return "".join(ans)
        
"""
Runtime: 92 ms, faster than 54.94% of Python online submissions for Reverse Vowels of a String.
Memory Usage: 14.9 MB, less than 76.55% of Python online submissions for Reverse Vowels of a String.
"""